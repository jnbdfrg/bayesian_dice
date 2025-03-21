# 🎲 Bayesian Dice

**Bayesian Dice** is a lightweight Python package for performing Bayesian inference on the fairness of dice based on observed rolls.

---

## 📌 Purpose

This package helps you:

- Simulate and analyze dice rolls.
- Perform Bayesian updates to estimate fairness.
- Visualize posterior distributions.
- Optionally perform Bayesian model comparison (e.g., fair vs. biased).

It’s ideal for learning Bayesian inference, demonstrating model selection, or just analyzing randomness in a fun way.

---

## 📦 Package Structure

```
bayesian_dice/
├── __init__.py
├── dice.py       # Core Bayesian logic
├── visuals.py    # Posterior plotting tools
tests/
└── test_dice.py  # Unit tests
```

---

## 🔍 Key Features

### 🎲 `BayesianDice` Class
Located in `dice.py`:

```python
from bayesian_dice.dice import BayesianDice

dice = BayesianDice()
dice.update([1, 2, 3, 6, 6, 6])
```

- `roll(n)`: Simulate `n` dice rolls.
- `update(rolls)`: Update beliefs based on observed rolls.
- `get_posterior()`: Get Beta distributions for each die face.

---

### 📊 `plot_posterior(dice)`
From `visuals.py`, used to plot the posterior probability of each side:

```python
from bayesian_dice.visuals import plot_posterior

plot_posterior(dice)
```

---

## 🧐 Concepts Behind the Package

- **Bayesian Inference**: Updates belief about dice fairness using observed evidence.
- **Posterior Distributions**: Each die face gets a Beta distribution.
- **Visualization**: Clear plots for intuitive understanding of fairness.

---

## 💡 Example

```python
from bayesian_dice.dice import BayesianDice
from bayesian_dice.visuals import plot_posterior

dice = BayesianDice()
dice.update([1, 2, 6, 6, 6, 3])
plot_posterior(dice)
```

---

## 🔮 Future Ideas

- Bayes Factor calculation (e.g., Savage-Dickey ratio)
- Sequential randomness tests
- Application to pseudorandom number analysis (e.g., gambling fairness)

---

## ⚖️ Bayes Factor Support

A future extension of this package includes computing **Bayes Factors** to compare models:

- `H0`: The die is fair (uniform distribution).
- `H1`: The die is biased (some faces are more likely).

The **Savage-Dickey density ratio** can be used to compute a Bayes Factor between these models. This would let users answer questions like:

> "How much more likely is it that the die is biased than fair, given the observed rolls?"

This can provide a principled way to **select between competing models** using Bayesian model comparison.

### 🧠 Interpreting the Result

| Bayes Factor (BF_01) | Interpretation                |
|----------------------|-------------------------------|
| > 3                  | Moderate evidence for fairness |
| ~1                   | Inconclusive                   |
| < 1                  | Evidence favors bias           |

---

## 📜 License

MIT License — use it, modify it, and share it freely.

