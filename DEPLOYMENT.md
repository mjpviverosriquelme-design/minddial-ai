# MindDial AI deployment checklist

## Status
The application code is in this repository. **The trained model binary files are not in this repository yet.** Deployment can serve the UI, but actual `/api/evaluate` requests will return HTTP 503 until all four compatible trained models are available.

## Setup
1. Verify each candidate's actual holdout accuracy and exact feature preprocessing.
2. Place validated `circle.joblib`, `numbers.joblib`, `placement.joblib`, `hands.joblib` under `models/`. Files must be compatible with `ml.py`, or replace each criterion's predictor with its own preprocessing. Avoid uploading any personal participant data.
3. Configure a private hosting service with persistent disk, TLS, and environment secret `MINDDIAL_REVIEW_TOKEN`. `render.yaml` is a suggested Render blueprint, **not an active deployment**.
4. Review storage, consent, authentication, retention, and access controls before inviting participants. The single review token and SQLite prototype are not production-grade security.
5. Run smoke tests with sample images, then verify all four predictions and the reviewer workflow.

## Run locally
```bash
pip install -r requirements.txt
export MINDDIAL_REVIEW_TOKEN='set-a-strong-secret'
uvicorn app:app --host 127.0.0.1 --port 8000
```
Open http://127.0.0.1:8000. The health endpoint at `/health` reports whether the four baseline files are present.

**Research prototype only.** The result is not a medical diagnosis. Do not use GitHub Pages for real inference or store identifiable patient data in the repository.
