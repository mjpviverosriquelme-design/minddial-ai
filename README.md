# MindDial AI — Warm & Friendly

Responsive, English-language, senior-friendly research prototype for Clock Drawing Test screening, with four modular AI prediction functions and human review.

## Run locally

```bash
pip install -r requirements.txt
export MINDDIAL_REVIEW_TOKEN="choose-a-strong-private-token"  # macOS/Linux
uvicorn app:app --reload
```

On Windows PowerShell: `$env:MINDDIAL_REVIEW_TOKEN="choose-a-strong-private-token"`.
Open http://127.0.0.1:8000.

`static/index.html` alone supports only the explicitly labeled fictional sample. Real predictions require the Python backend. GitHub Pages can host a static interface, **not** the Python inference API; production deployment needs a separate secure server.

**Model selection:** see `MODEL_SELECTION.md`. The bundle still includes the existing SVM baseline models, not the higher-accuracy candidates until their trained artifacts and preprocessing are verified. Reviewers can adjust each binary score and save through the API when authenticated.

**Privacy:** demographic data are optional and saved only with consent. This prototype is not production-ready for identifiable health information. Do not expose the reviewer token in public code. Authentication, encryption, data retention, consent processes, and independent clinical validation are required before real participant use. The result is not a diagnosis.