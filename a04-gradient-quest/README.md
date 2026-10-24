# Block Builders — A04 ITAI 2376
Author: María José Viveros Riquelme. Team name pending.
Submission name: A04_[TeamName]_MariaJoseViverosRiquelme_ITAI2376

A bilingual building-block game for an 11-year-old audience. Each challenge starts with a simple explanation and concrete example before play.

1. Match a 6-block example: count extra/missing blocks and correct your tower.
2. Match a 9-block example with 1-, 2-, or 4-block changes: discover overshooting.
3. Train a robot to match 7 blocks: try Giant first, then reduce the update size.
4. Explain why comparing, adjusting and repeating helps learning.

The first two challenges are manual analogies. The robot uses the gradient of L(w)=(w-target)^2 with alpha=0.05, 0.25, or 1; updates are rounded to whole blocks, minimum one while error remains. This is quantized gradient descent, not exact continuous optimization. Updates outside 0–16 are rejected. The visible difference is absolute difference, not squared loss. No actual neural network is trained. Full technical limitations and sources appear in the game.

Open dist/index.html directly to play offline. No dependencies or accounts required. Original building-game-inspired SVG art; no affiliation with Minecraft or LEGO. Prepared with AI assistance; review before submitting.

References:
Google for Developers. (n.d.). Linear regression: Gradient descent. https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent
Google for Developers. (n.d.). Linear regression: Hyperparameters. https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters
Accessed October 23, 2026.
