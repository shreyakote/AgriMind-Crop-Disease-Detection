from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "demo"

classes = ["healthy", "diseased"]

for cls in classes:
    folder = DATA / cls
    folder.mkdir(parents=True, exist_ok=True)

    for i in range(20):
        file = folder / f"{i}.txt"
        file.write_text(f"sample image: {cls}\n")

print("Demo dataset created successfully!")
print("Healthy: 20")
print("Diseased: 20")