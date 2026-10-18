"""Deployment smoke test: validates four real trained artifacts and their feature dimensions.
This is not a clinical validation or browser parity test.
"""
from pathlib import Path
import joblib
import numpy as np
import cv2
from skimage.feature import hog

root = Path(__file__).resolve().parents[1]
gray = np.full((256, 256), 255, dtype=np.uint8)
cv2.circle(gray, (128, 128), 95, 0, 3)
gray = cv2.resize(gray, (128, 128), interpolation=cv2.INTER_AREA)
gray = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8)).apply(gray)
x = hog(gray, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(2, 2), block_norm="L2-Hys").astype("float32").reshape(1, -1)
for name in ("circle", "numbers", "placement", "hands"):
    path = root / "models" / (name + ".joblib")
    assert path.is_file() and path.stat().st_size > 1000, f"Missing model: {name}"
    model = joblib.load(path)
    assert model.n_features_in_ == x.shape[1], f"Feature mismatch: {name}"
    prediction = int(model.predict(x)[0])
    assert prediction in (0, 1), f"Invalid prediction: {name}"
    print(f"{name}: OK ({prediction})")
print("Python model smoke test passed. Browser parity remains unverified.")
