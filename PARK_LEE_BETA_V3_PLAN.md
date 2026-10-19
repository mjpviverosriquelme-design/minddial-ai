# MindDial AI Beta v3 — Park & Lee-inspired implementation plan

## Scope
Academic Clock Drawing Test prototype using a modular architecture inspired by Park & Lee (2021), **not a reproduction of their trained models or reported performance**. Input is a static uploaded/drawn image, not mobile stylus trajectories or motion sensors. Preserve four binary scores (closed circle, 12 numbers, correct placement, hands at 11:10), sum 0–4; PASS at >=3 is a project convention, not a clinical diagnosis.

## Components
1. DeepC: lightweight U-Net segmentation of circle contour; assess continuity/closure via geometric postprocessing.
2. DeepN: detect individual handwritten numerals (including two-digit numbers 10,11,12), then recognize and deduplicate them. MNIST may initialize digit recognition, but domain-specific clock labels are required.
3. DeepH: lightweight U-Net segmentation of hands; distinguish hands from circle/numeral strokes and estimate two orientations and lengths.
4. Geometry integration: circle center and radius; normalize angles; verify all 12 distinct numbers and their angular positions; verify two hands at 11 and 2 (11:10); generate four auditable binary scores.

## Data readiness and safeguards
Current 363 real clock images have image-level binary labels, **not** pixel segmentation masks or numeral bounding boxes. These must be annotated and quality-reviewed before U-Net/detection training. Prior 1000 generated images can augment *training only*; they must never appear in final real holdout. Group splits by participant where possible. Do not upload identifiable participant images or private datasets to public GitHub.

## Execution gates
A. Audit actual available data, permissions and class balance; freeze participant-level real holdout.
B. Produce and inspect annotations for contour, numeral boxes/IDs, hands; verify inter-annotator agreement on a sample.
C. Train DeepC/DeepH segmentation, DeepN recognition and compare against baseline HOG models.
D. Measure segmentation Dice/IoU, numeral detection mAP/recall, recognition accuracy, and per-criterion sensitivity, specificity, balanced accuracy, F1 on untouched real holdout. Target >=0.80 balanced accuracy **per criterion**; do not claim it until demonstrated.
E. Build deterministic geometric scorer, add negative unit tests: blank closed circle [1,0,0,0], open circle [0,0,0,0], complete correct clock [1,1,1,1], missing hands [1,1,1,0] when numerals positioned correctly.
F. Package model weights + preprocessing version, implement inference pipeline; compare Python/web outputs image by image. Deploy only after checks pass and with user-approved repository visibility. Do not substitute fixed/mock predictions.

## Immediate next action
Create component-level annotations from available real clock images, with quality review. Existing four binary labels alone cannot train U-Net segmentation. No Park & Lee neural models have yet been trained or deployed in this repo.
