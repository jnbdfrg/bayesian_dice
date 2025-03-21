from bayesian_dice.dice import BayesianDice

dice = BayesianDice()
dice.update([6, 6, 6, 3, 1, 2, 4, 5, 6, 6])  # biased toward 6

# Compute Bayes Factor for side 6 (index 5)
bf = dice.bayes_factor(side=5)
print(f"Bayes Factor for H0 (side 6 fair): {bf:.3f}")

print(dice.interpret_bayes_factor(side=5))
