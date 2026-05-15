import os
import json
import logging
import joblib
import pandas as pd
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

# ─── Logging ──────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Works for both Railway Docker (/app) and local dev (../models)
if os.path.exists(os.path.join(BASE_DIR, "models")):
    MODELS_DIR   = os.path.join(BASE_DIR, "models")
    API_DIR      = os.path.join(BASE_DIR, "api")
    DATA_OUT_DIR = os.path.join(BASE_DIR, "data")
else:
    MODELS_DIR   = os.path.join(BASE_DIR, "..", "models")
    API_DIR      = os.path.join(BASE_DIR, "..", "api")
    DATA_OUT_DIR = os.path.join(BASE_DIR, "..", "data")

MODEL_PATH        = os.path.join(MODELS_DIR, "xgboost_model.pkl")
PREPROCESSOR_PATH = os.path.join(MODELS_DIR, "preprocessor.pkl")
SEGMENTS_PATH     = os.path.join(API_DIR,    "segmentation_insights.json")

# ─── Global state ─────────────────────────────────────────────────────────────
_state: dict = {
    "model":            None,
    "preprocessor":     None,
    "segmentation_data": {},
}

# ─── Lifespan ─────────────────────────────────────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    """Load ML artefacts on startup; log results clearly."""
    # Model + preprocessor
    for label, path, key in [
        ("XGBoost model",   MODEL_PATH,        "model"),
        ("Preprocessor",    PREPROCESSOR_PATH, "preprocessor"),
    ]:
        if os.path.exists(path):
            try:
                _state[key] = joblib.load(path)
                logger.info("%s loaded successfully from %s", label, path)
            except Exception as exc:
                logger.error("Failed to load %s: %s", label, exc)
        else:
            logger.warning("%s not found at %s — run pipeline.py first.", label, path)

    # Segmentation insights
    if os.path.exists(SEGMENTS_PATH):
        try:
            with open(SEGMENTS_PATH, "r") as f:
                _state["segmentation_data"] = json.load(f)
            logger.info("Segmentation data loaded successfully.")
        except Exception as exc:
            logger.error("Failed to load segmentation data: %s", exc)
    else:
        logger.warning("Segmentation insights not found at %s", SEGMENTS_PATH)

    yield  # ← app runs here

    logger.info("Shutting down API.")


# ─── App ──────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="Customer Churn Intelligence API",
    description="Predict customer churn probability and explore segmentation analytics.",
    version="2.1.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Global exception handler ─────────────────────────────────────────────────
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error("Unhandled exception on %s: %s", request.url.path, exc)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error. Please try again later."},
    )


# ─── Schema ───────────────────────────────────────────────────────────────────
class CustomerData(BaseModel):
    CreditScore:     int   = Field(..., ge=300, le=900,  example=619)
    Geography:       str   = Field(...,                  example="France")
    Gender:          str   = Field(...,                  example="Female")
    Age:             int   = Field(..., ge=18,  le=100,  example=42)
    Tenure:          int   = Field(..., ge=0,   le=10,   example=2)
    Balance:         float = Field(..., ge=0.0,          example=0.0)
    NumOfProducts:   int   = Field(..., ge=1,   le=4,    example=1)
    HasCrCard:       int   = Field(..., ge=0,   le=1,    example=1)
    IsActiveMember:  int   = Field(..., ge=0,   le=1,    example=1)
    EstimatedSalary: float = Field(..., ge=0.0,          example=101348.88)


# ─── Routes ───────────────────────────────────────────────────────────────────
@app.get("/health", tags=["System"])
def health_check():
    """Liveness probe — used by Railway's healthcheck."""
    return {
        "status":       "ok",
        "model_loaded": _state["model"] is not None,
        "data_loaded":  bool(_state["segmentation_data"]),
    }


@app.post("/predict", tags=["Prediction"])
def predict_churn(customer: CustomerData):
    """Return churn probability, binary prediction, and risk level."""
    if _state["model"] is None or _state["preprocessor"] is None:
        raise HTTPException(
            status_code=503,
            detail="Model not ready. Please contact the administrator.",
        )

    data = customer.model_dump()
    df   = pd.DataFrame([data])

    # Feature engineering — must mirror pipeline.py
    df["BalanceSalaryRatio"]   = df["Balance"] / (df["EstimatedSalary"] + 1e-6)
    df["AgeTenureInteraction"] = df["Age"] * df["Tenure"]
    df["ProductUsageDensity"]  = df["NumOfProducts"] / (df["Tenure"] + 1)

    try:
        X_proc = _state["preprocessor"].transform(df)
        prob   = float(_state["model"].predict_proba(X_proc)[0, 1])
        pred   = int(_state["model"].predict(X_proc)[0])
    except Exception as exc:
        logger.error("Prediction failed: %s", exc)
        raise HTTPException(status_code=400, detail=f"Prediction error: {exc}")

    risk_level = "High" if prob > 0.7 else ("Medium" if prob > 0.4 else "Low")

    logger.info(
        "Prediction: prob=%.4f | pred=%d | risk=%s | customer=%s",
        prob, pred, risk_level, data,
    )

    return {
        "churn_probability": round(prob, 4),
        "prediction":        pred,
        "risk_level":        risk_level,
    }


@app.get("/segments", tags=["Analytics"])
def get_segments():
    """Return full segmentation analytics dataset."""
    if not _state["segmentation_data"]:
        raise HTTPException(
            status_code=404,
            detail="Segmentation data not found. Run pipeline.py first.",
        )
    return _state["segmentation_data"]


@app.get("/metrics", tags=["Analytics"])
def get_metrics():
    """Return high-level KPIs: churn rate, total customers, active users."""
    sd = _state["segmentation_data"]
    if not sd:
        raise HTTPException(
            status_code=404,
            detail="Metrics not found. Run pipeline.py first.",
        )
    return {
        "overall_churn_rate": round(sd.get("overall_churn_rate", 0) * 100, 2),
        "total_customers":    sd.get("total_customers", 0),
        "active_users":       sd.get("active_users", 0),
    }


# ─── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn

    # Railway injects PORT; fall back to 8000 locally
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
