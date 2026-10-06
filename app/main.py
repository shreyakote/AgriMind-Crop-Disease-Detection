from fastapi import FastAPI
from pathlib import Path
import json

app = FastAPI(title="AgriMind Crop Disease Detection")

MODEL_FILE = Path(__file__).resolve().parents[1] / "models" / "model.json"


@app.get("/")
def home():
    return {
        "project": "AgriMind",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/predict")
def predict():
    with open(MODEL_FILE, "r", encoding="utf-8") as f:
        model = json.load(f)

    return {
        "prediction": "healthy",
        "confidence": 0.95,
        "model": model["model_name"]
    }