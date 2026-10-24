# Gradient Quest — A04 ITAI 2376

**Author:** María José Viveros Riquelme  
**Team:** pending confirmation  
**Submission name:** `A04_[TeamName]_MariaJoseViverosRiquelme_ITAI2376`  
**Topic:** Gradient Descent  
**Audience:** age 11; approximately 5 minutes  
**Due:** October 31, 2026, 11:59 PM (course deadline; verify Canvas timezone).

## Play
Open `dist/index.html` directly in a modern browser. No installation, account, API key, or model download is required. English/Spanish toggle included. The optional Google Fonts request falls back to system fonts offline.

1. Mission 1: choose the downhill direction.
2. Mission 2: compare Tiny (0.04), Steady (0.20), and Giant (1.05) learning rates. Observe loss rise with an oversized update; recover with a smaller rate.
3. Mission 3: reach loss < 0.10 in at most 8 updates.
4. Explain what AI adjusts and why.

## Concept and implementation
A deterministic educational simulation computes L(w)=(w−2)^2, gradient=2(w−2), and w_next=w−alpha*gradient. Pip's horizontal position represents a weight; vertical height represents loss. This is a convex, one-parameter illustration, not an actual trained deep neural network. Real networks optimize many parameters on more complex landscapes; a global minimum is not guaranteed. Backpropagation computes gradients; gradient descent updates parameters using them.

## Short presentation script
“Imagine Pip is learning to make better predictions. The higher Pip stands, the more mistakes it makes. The slope tells us which way error grows; Pip moves the opposite way. Our learning rate controls each update. Let's try a giant step: Pip jumps past the bottom and the error rises. A moderate step works better here. Neural networks also measure prediction error and repeatedly adjust their weights. This valley simplifies that process so we can see it happen.”

Ask the learner: Which way reduces error? What happens with a huge learning rate? What does Pip's position represent? Success means explaining the idea, not only finishing the game.

## Primary references
Google for Developers. (n.d.). *Linear regression: Gradient descent*. Machine Learning Crash Course. Retrieved October 23, 2026, from https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent

Google for Developers. (n.d.). *Linear regression: Hyperparameters*. Machine Learning Crash Course. Retrieved October 23, 2026, from https://developers.google.com/machine-learning/crash-course/linear-regression/hyperparameters

## Credits and submission
Original interface and SVG artwork prepared with AI assistance. Review the game, supply the actual team name, and ensure the final explanation reflects your understanding before submitting. No player data is collected or stored.

The GitHub branch is separate from MindDial AI's main branch. This assignment does not change the MindDial application.
