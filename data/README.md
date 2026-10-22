# Clock Drawing Test — MindDial AI (master dataset)

This directory contains the master scoring spreadsheet for **400 clock drawings** (Clock_001 to Clock_400).

- [Excel master file](Original_Master_Evaluation.xlsx) — three worksheets: Ground_Truth, Instructions, Summary.
- [CSV for in-browser viewing](Clock_Drawing_Master_Evaluation.csv) — the 400 records from Ground_Truth; open on GitHub to preview the table.

## Fields

Each record has an image ID and four human-scored binary criteria (0 = not met; 1 = met): closed circle, correct number position, all 12 numbers, and correct hand positions. `Human_Total` ranges from 0 to 4. `Notes` is optional.

This is an experimental educational dataset. These scores should **not** be interpreted as a validated medical diagnosis, nor as evidence of clinical diagnostic accuracy. Images are not included in these files.

The publicly shared Excel copy is based on the original master workbook; personally identifying document-editor metadata was removed without changing the dataset cells or worksheets.
