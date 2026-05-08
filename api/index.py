"""
Vercel Serverless Function — FastAPI backend for Customer Churn Intelligence.
All routes are served under /api/* via Vercel rewrites.
"""
import os
import json
import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from mangum import Mangum

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)  # project root

MODELS_DIR = os.path.join(ROOT_DIR, 'models')
DATA_OUT_DIR = os.path.join(ROOT_DIR, 'data')

MODEL_PATH = os.path.join(MODELS_DIR, 'xgboost_model.pkl')
PREPROCESSOR_PATH = os.path.join(MODELS_DIR, 'preprocessor.pkl')
SEGMENTS_PATH = os.path.join(DATA_OUT_DIR, 'segmentation_insights.json')

# ─── Global state (loaded once per cold start) ───────────────────────────────
_model = None
_preprocessor = None
_segmentation_data = {}


def _load():
    global _model, _preprocessor, _segmentation_data
    if _model is None:
        try:
            _model = joblib.load(MODEL_PATH)
            _preprocessor = joblib.load(PREPROCESSOR_PATH)
            print("Model and preprocessor loaded successfully.")
        except Exception as e:
            print(f"Warning: Could not load model/preprocessor: {e}")

    if not _segmentation_data:
        try:
            with open(SEGMENTS_PATH, 'r') as f:
                _segmentation_data = json.load(f)
            print("Segmentation data loaded successfully.")
        except Exception as e:
            print(f"Warning: Could not load segmentation data: {e}")


_load()

# ─── App ──────────────────────────────────────────────────────────────────────
app = FastAPI(
    title="Customer Churn Intelligence API",
    version="2.0.0",
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
@app.get("/api/health")
def health_check():
    return {
        "status": "ok",
        "model_loaded": _model is not None,
        "data_loaded": bool(_segmentation_data),
    }


@app.post("/api/predict")
def predict_churn(customer: CustomerData):
    if _model is None or _preprocessor is None:
        raise HTTPException(status_code=503, detail="Model not loaded. Run pipeline.py first.")

    data = customer.model_dump()
    df = pd.DataFrame([data])

    # Feature engineering (must mirror pipeline.py)
    df['BalanceSalaryRatio'] = df['Balance'] / (df['EstimatedSalary'] + 1e-6)
    df['AgeTenureInteraction'] = df['Age'] * df['Tenure']
    df['ProductUsageDensity'] = df['NumOfProducts'] / (df['Tenure'] + 1)

    try:
        X_proc = _preprocessor.transform(df)
        prob = float(_model.predict_proba(X_proc)[0, 1])
        pred = int(_model.predict(X_proc)[0])

        if prob > 0.7:
            risk_level = "High"
        elif prob > 0.4:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        return {
            "churn_probability": round(prob, 4),
            "prediction": pred,
            "risk_level": risk_level,
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Prediction error: {e}")


@app.get("/api/segments")
def get_segments():
    if not _segmentation_data:
        raise HTTPException(status_code=404, detail="Segmentation data not found.")
    return _segmentation_data


@app.get("/api/metrics")
def get_metrics():
    if not _segmentation_data:
        raise HTTPException(status_code=404, detail="Metrics not found.")
    return {
        "overall_churn_rate": round(_segmentation_data.get('overall_churn_rate', 0) * 100, 2),
        "total_customers": _segmentation_data.get('total_customers', 0),
        "active_users": _segmentation_data.get('active_users', 0),
    }


# ─── Vercel ASGI handler ─────────────────────────────────────────────────────
handler = Mangum(app, lifespan="off")
