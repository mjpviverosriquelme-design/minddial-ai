# Model selection and integration status

MindDial AI calls four independent functions in `ml.py`: `predict_circle`, `predict_numbers`, `predict_placement`, `predict_hands`. Each returns a binary prediction and optional confidence. Their outputs are summed (0–4) and remain subject to human review.

## Experimental accuracy targets (NOT the accuracy of the currently packaged files)

| Criterion | Candidate best accuracy | Status |
| --- | --- | --- |
| Closed circle | 87% Gradient Boosting | Candidate result; matching serialized model and preprocessing not verified |
| All 12 numbers | 84.25% | Candidate result; matching serialized model not verified |
| Number placement | 63.5% Random Forest | Candidate result; existing independent artifact needs compatible preprocessing verification |
| Hands | 70.75% | Candidate result; matching serialized model not verified |

## Models currently runnable in this bundle

The four bundled files in `models/` are the existing HOG+SVM baseline, **not** the higher-accuracy experimental candidates. Their recorded accuracy values are in `models/validation.json`. The frontend does not misrepresent these baselines as the selected experimental models.

To activate a superior model: recover its trained artifact, reproduce its original image transformations, evaluate on an untouched comparable holdout set, then replace only the corresponding `predict_*` function. Never substitute a `.joblib` file unless feature compatibility is confirmed. Do not use age, gender or ethnicity as prediction features.