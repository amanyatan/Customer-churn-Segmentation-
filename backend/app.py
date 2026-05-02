import os
import json
import joblib
import pandas as pd
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR       = os.path.dirname(os.path.abspath(__file__))

# Check if we are running inside Docker (WORKDIR /app) or locally
if os.path.exists(os.path.join(BASE_DIR, 'models')):
    # Docker path: /app/models
    MODELS_DIR = os.path.join(BASE_DIR, 'models')
    DATA_OUT_DIR = os.path.join(BASE_DIR, 'data')
else:
    # Local path: ../models
    MODELS_DIR = os.path.join(BASE_DIR, '..', 'models')
    DATA_OUT_DIR = os.path.join(BASE_DIR, '..', 'data')

MODEL_PATH      = os.path.join(MODELS_DIR, 'xgboost_model.pkl')
PREPROCESSOR_PATH = os.path.join(MODELS_DIR, 'preprocessor.pkl')
SEGMENTS_PATH  = os.path.join(DATA_OUT_DIR, 'segmentation_insights.json')
DATASET_PATH   = os.path.join(DATA_OUT_DIR, 'European_Bank.csv')

# ─── Global state ─────────────────────────────────────────────────────────────
_state = {
    "model": None,
    "preprocessor": None,
    "segmentation_data": {},
}

# ─── Lifespan (replaces deprecated on_event) ──────────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    try:
        _state["model"]        = joblib.load(MODEL_PATH)
        _state["preprocessor"] = joblib.load(PREPROCESSOR_PATH)
        print("Model and preprocessor loaded successfully.")
    except Exception as e:
        print(f"Warning: Could not load model/preprocessor. Run pipeline.py first.\n   Error: {e}")

    try:
        with open(SEGMENTS_PATH, 'r') as f:
            _state["segmentation_data"] = json.load(f)
        print("Segmentation data loaded successfully.")
    except Exception as e:
        print(f"Warning: Could not load segmentation data. Run pipeline.py first.\n   Error: {e}")

    yield  # Application runs here

    # Shutdown (nothing special needed)
    print("Shutting down.")


# ─── App ──────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="Customer Churn Intelligence API",
    version="2.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─── Schema ───────────────────────────────────────────────────────────────────
class CustomerData(BaseModel):
    CreditScore:      int   = Field(..., json_schema_extra={"example": 619})
    Geography:        str   = Field(..., json_schema_extra={"example": "France"})
    Gender:           str   = Field(..., json_schema_extra={"example": "Female"})
    Age:              int   = Field(..., json_schema_extra={"example": 42})
    Tenure:           int   = Field(..., json_schema_extra={"example": 2})
    Balance:          float = Field(..., json_schema_extra={"example": 0.0})
    NumOfProducts:    int   = Field(..., json_schema_extra={"example": 1})
    HasCrCard:        int   = Field(..., json_schema_extra={"example": 1})
    IsActiveMember:   int   = Field(..., json_schema_extra={"example": 1})
    EstimatedSalary:  float = Field(..., json_schema_extra={"example": 101348.88})


# ─── Routes ───────────────────────────────────────────────────────────────────
@app.get("/health")
def health_check():
    """Quick liveness probe for the frontend to check if API is up."""
    return {
        "status": "ok",
        "model_loaded": _state["model"] is not None,
        "data_loaded":  bool(_state["segmentation_data"]),
    }


@app.post("/predict")
def predict_churn(customer: CustomerData):
    if _state["model"] is None or _state["preprocessor"] is None:
        raise HTTPException(status_code=503, detail="Model not loaded. Run pipeline.py first.")

    data = customer.model_dump()
    df   = pd.DataFrame([data])

    # Feature engineering (must mirror pipeline.py)
    df['BalanceSalaryRatio']   = df['Balance'] / (df['EstimatedSalary'] + 1e-6)
    df['AgeTenureInteraction'] = df['Age'] * df['Tenure']
    df['ProductUsageDensity']  = df['NumOfProducts'] / (df['Tenure'] + 1)

    try:
        X_proc = _state["preprocessor"].transform(df)
        prob   = float(_state["model"].predict_proba(X_proc)[0, 1])
        pred   = int(_state["model"].predict(X_proc)[0])

        if prob > 0.7:
            risk_level = "High"
        elif prob > 0.4:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        return {
            "churn_probability": round(prob, 4),
            "prediction":        pred,
            "risk_level":        risk_level,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {e}")


@app.get("/segments")
def get_segments():
    if not _state["segmentation_data"]:
        raise HTTPException(status_code=404, detail="Segmentation data not found. Run pipeline.py first.")
    return _state["segmentation_data"]


@app.get("/metrics")
def get_metrics():
    sd = _state["segmentation_data"]
    if not sd:
        raise HTTPException(status_code=404, detail="Metrics not found. Run pipeline.py first.")
    return {
        "overall_churn_rate": round(sd.get('overall_churn_rate', 0) * 100, 2),
        "total_customers":    sd.get('total_customers', 0),
        "active_users":       sd.get('active_users', 0),
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
