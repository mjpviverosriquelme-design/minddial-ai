# MindDial AI — Beta v2 retraining (academic experiment)

A new local training run was completed using **363 labeled clock images** from the 400-row annotation workbook. Each image was processed using OpenCV grayscale, resize 128×128, CLAHE, and HOG (8100 features). Four independently trained classifiers were fitted. A 25% holdout (91 images) was used for exploratory model selection; therefore these metrics are **not independent external validation**.

| Criterion | Selected model | Exploratory accuracy |
|---|---|---:|
| Closed circle | SVM RBF | 78.02% |
| All 12 numbers | SVM RBF with 180 synthetic blank-circle hard negatives | 83.52% (original holdout before hard-negative augmentation; post-augmentation same accuracy) |
| Number placement | Random Forest | 62.64% |
| Hands | SVM RBF with 180 synthetic blank-circle/partial-hand hard negatives | 69.23% |

The synthetic hard-negative examples have *known negative labels* for numbers and hands; they are supplemental training examples, not simulated predictions. A local smoke check predicted **[1,0,0,0]** on a blank circle and **[1,1,0,1]** on a complete hand-drawn clock. The latter is not fully correct: placement remains an open issue.

**Deployment status:** The updated `.joblib` files were produced locally and bundled as `MindDial_AI_Beta_v2_Models.zip`, but have **not yet been uploaded to this GitHub repository**. GitHub Pages currently serves whichever model files are committed under `models/`. Upload the four updated files to those exact paths, commit, and verify the GitHub Actions deployment. Do not claim v2 is live before that is confirmed.

**Browser parity:** The website currently uses scikit-image approximations for OpenCV resize/CLAHE, so parity against the training pipeline is not established. Do not claim model parity or validated accuracy until identical-image tests pass.

This is a coursework research beta, not a clinical diagnostic tool. Do not commit private participant images or personal data.
