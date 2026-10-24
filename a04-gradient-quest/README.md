# El mundo de los errores — Expectativa vs. realidad

María José Viveros Riquelme · ITAI 2376 · A04. Team name pending.

A Christmas mini-game in an 8-bit-inspired interface with original pixel SVG gifts, family portraits, a red panda and optional procedural chiptune music.

The player predicts one of 15 gifts for each of five relatives: younger sister, older brother, grandfather, parents, and aunt. Each actual gift is assigned before predictions and remains fixed for the round. The five actual gifts cover five categories, with three gift alternatives in each category. Predictions may repeat.

Scoring: identical gift -> 3 points / loss 0; same category, different gift -> 2 points / loss 1; different category -> 1 point / loss 2. Total loss ranges from 0 to 10; mean is total divided by five. Loss = 3 - score. The custom categorical loss is an educational rule, not a universal emotion measure. Reactions concern the gift mismatch, not the worth of a relative.

Concepts: prediction, observed outcome, category similarity, loss function, total loss, mean loss, and revising predictions after feedback. The machine applies rules; no trained AI model is claimed. Replaying the same gifts demonstrates using known outcomes, not generalization. New Christmas creates new hidden outcomes.

Assignment scope: this is a loss-function module that can introduce Backpropagation; it does not yet teach the full backpropagation algorithm or run gradient descent. The discrete loss is not differentiated.

Play by opening dist/index.html, or use the hosted public page. No dependencies, keys or sign-in needed. Explanatory intro appears before play. Sound starts only through explicit opt-in and pauses when hidden.

Reference: Google for Developers. (n.d.). Linear regression: Loss. https://developers.google.com/machine-learning/crash-course/linear-regression/loss (accessed October 23, 2026). The gift scale is an original adaptation.

Checks: all 225 gift comparison pairs, full five-turn state flow, total/mean loss, fixed outcomes, replay and improved predictions passed Node-based DOM simulation. Browser preview verified gift selection and reveal scoring.
