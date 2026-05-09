"""
Vercel Serverless Function — FastAPI backend for Customer Churn Intelligence.
All routes are served under /api/* via Vercel rewrites.
This version uses pure Python for inference to avoid Vercel's 250MB limit!
"""
import os
import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from mangum import Mangum
from . import xgboost_pure

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)  # project root

DATA_OUT_DIR = os.path.join(ROOT_DIR, 'data')
SEGMENTS_PATH = os.path.join(DATA_OUT_DIR, 'segmentation_insights.json')
CONFIG_PATH = os.path.join(BASE_DIR, 'preprocessor_config.json')

# ─── Global state (loaded once per cold start) ───────────────────────────────
_segmentation_data = {}
_preprocessor_config = {}

def _load():
    global _segmentation_data, _preprocessor_config
    if not _segmentation_data:
        try:
            with open(SEGMENTS_PATH, 'r') as f:
                _segmentation_data = json.load(f)
            print("Segmentation data loaded successfully.")
        except Exception as e:
            print(f"Warning: Could not load segmentation data: {e}")

    if not _preprocessor_config:
        try:
            with open(CONFIG_PATH, 'r') as f:
                _preprocessor_config = json.load(f)
            print("Preprocessor config loaded successfully.")
        except Exception as e:
            print(f"Warning: Could not load preprocessor config: {e}")


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
        "data_loaded": bool(_segmentation_data),
        "pure_python_mode": True
    }


@app.post("/api/predict")
def predict_churn(customer: CustomerData):
    if not _preprocessor_config:
        raise HTTPException(status_code=503, detail="Config not loaded.")

    data = customer.model_dump()

    # Feature engineering (must mirror pipeline.py)
    data['BalanceSalaryRatio'] = data['Balance'] / (data['EstimatedSalary'] + 1e-6)
    data['AgeTenureInteraction'] = data['Age'] * data['Tenure']
    data['ProductUsageDensity'] = data['NumOfProducts'] / (data['Tenure'] + 1)

    try:
        # Preprocessing in pure python
        num_features = _preprocessor_config["num_features"]
        means = _preprocessor_config["means"]
        scales = _preprocessor_config["scales"]
        
        vector = []
        
        # 1. Standard Scaler
        for i, feat in enumerate(num_features):
            val = data[feat]
            scaled_val = (val - means[i]) / scales[i]
            vector.append(scaled_val)
            
        # 2. One Hot Encoder
        cat_features = _preprocessor_config["cat_features"]
        categories = _preprocessor_config["categories"]
        
        for i, feat in enumerate(cat_features):
            val = data[feat]
            cats = categories[i]
            # OHE logic: create 0s and 1s
            for cat in cats:
                vector.append(1.0 if val == cat else 0.0)
                
        # Inference using pure python xgboost model
        # m2cgen outputs the log-odds for binary classification
        raw_score = xgboost_pure.score(vector)
        if isinstance(raw_score, list):
            prob = raw_score[1]
        else:
            prob = xgboost_pure.sigmoid(raw_score)
        pred = 1 if prob > 0.5 else 0

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
            "pure_python": True
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
