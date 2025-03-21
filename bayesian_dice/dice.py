import random
import numpy as np
from scipy.stats import beta

class BayesianDice:
    def __init__(self, sides=6, alpha=1, beta=1):
        self.sides = sides
        self.alpha = np.ones(sides) * alpha
        self.beta = np.ones(sides) * beta
        self.observations = np.zeros(sides)

    def roll(self, n=1):
        """Simulates rolling a die `n` times."""
        return [random.randint(1, self.sides) for _ in range(n)]

    def update(self, rolls):
        """Updates beliefs using Bayesian inference."""
        for roll in rolls:
            self.observations[roll - 1] += 1
        self.alpha += self.observations

    def get_posterior(self):
        """Returns posterior probability for each face."""
        return [beta(a, b) for a, b in zip(self.alpha, self.beta)]
