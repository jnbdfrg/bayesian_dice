from bayesian_dice.dice import BayesianDice
from bayesian_dice.visuals import plot_posterior

# Create a dice instance
dice = BayesianDice()

# Simulate some dice rolls (you can change the numbers)
rolls = [1, 2, 2, 3, 3, 3, 4, 6, 6, 6, 6]

# Update belief based on the rolls
dice.update(rolls)

# Plot the posterior probability distribution
plot_posterior(dice)
