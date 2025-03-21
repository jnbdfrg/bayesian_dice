import sys
import os

# Ensure the parent directory is in the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bayesian_dice.dice import BayesianDice  # Now this should work

import unittest

class TestBayesianDice(unittest.TestCase):
    def test_rolls(self):
        dice = BayesianDice()
        rolls = dice.roll(10)
        self.assertEqual(len(rolls), 10)

    def test_update(self):
        dice = BayesianDice()
        rolls = [1, 2, 3, 3, 4, 5, 6, 6, 6, 6]
        dice.update(rolls)
        self.assertGreater(dice.alpha[5], 1)  # Side 6 should have more observations

if __name__ == "__main__":
    unittest.main()
