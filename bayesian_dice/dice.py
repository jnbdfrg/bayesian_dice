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

    def bayes_factor(self, side=0):
        """
        Compute the Bayes Factor using the Savage-Dickey ratio for one die face.

        Parameters:
            side (int): index of the die face to test (0-indexed, e.g., 0 for side 1)

        Returns:
            float: Bayes Factor (BF_01) for H0: theta = 1/sides
        """
        fair_value = 1.0 / self.sides

        # Prior and posterior for this side
        a_prior = self.beta[side]
        b_prior = sum(self.beta) - self.beta[side]

        a_post = self.alpha[side]
        b_post = sum(self.alpha) - self.alpha[side]

        prior_pdf = beta.pdf(fair_value, a_prior, b_prior)
        post_pdf = beta.pdf(fair_value, a_post, b_post)

        return prior_pdf / post_pdf

    def interpret_bayes_factor(self, side=0):
        """
        Interpret the Bayes Factor for a given die face.

        Returns:
            str: interpretation (e.g., 'Evidence supports bias')
        """
        bf = self.bayes_factor(side)
        if bf > 10:
            return "Strong evidence the die is fair."
        elif bf > 3:
            return "Moderate evidence the die is fair."
        elif bf > 1:
            return "Weak evidence the die is fair."
        elif bf > 1/3:
            return "Weak evidence the die is biased."
        elif bf > 1/10:
            return "Moderate evidence the die is biased."
        else:
            return "Strong evidence the die is biased."
