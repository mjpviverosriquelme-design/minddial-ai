# MindDial AI — GitHub Pages

This repository contains the **Warm & Friendly** clock-drawing research prototype.

## GitHub Pages setup
1. Repository Settings → Pages → Build and deployment → **GitHub Actions**.
2. The workflow `.github/workflows/pages.yml` will publish `static/index.html`.
3. On GitHub Free, the repository generally needs to be **public** to use Pages. Make sure it contains no personal participant data before changing visibility.

**Important:** GitHub Pages is static hosting. The existing `/api/evaluate` and `/api/review` Python endpoints **will not work** on GitHub Pages. The current HTML supports a labeled example mode, but cannot perform real AI inference there.

The four trained `.joblib` baseline models are only in the separate local Python ZIP, not in this repository. To enable genuine on-device inference, export each trained model to a browser-compatible representation, reproduce image preprocessing exactly, and validate parity with Python on held-out images. Do not present sample results as genuine predictions.

For now, run the local Python package for actual inference. This is a research prototype, not a medical diagnosis. No participant images or sensitive data should be committed to GitHub.

## Included experimental browser models

`browser.html` now downloads the four baseline SVM models automatically from `models/`. Optional trusted local replacements remain available. The drawings stay on the device. Clinical validity and browser/Python output parity have not been established. The homepage example mode remains illustrative; Python API endpoints are not hosted by Pages.
