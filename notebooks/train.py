from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "demo"
MODEL_DIR = ROOT / "models"

MODEL_DIR.mkdir(exist_ok=True)

classes = ["healthy", "diseased"]

data = {
    "model_name": "AgriMind Demo Classifier",
    "classes": classes,
    "dataset": {
        "healthy": len(list((DATA / "healthy").glob("*.txt"))),
        "diseased": len(list((DATA / "diseased").glob("*.txt")))
    },
    "status": "trained"
}

model_file = MODEL_DIR / "model.json"

with open(model_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Model created successfully!")
print(f"Model saved to: {model_file}")
print("Classes:", classes)