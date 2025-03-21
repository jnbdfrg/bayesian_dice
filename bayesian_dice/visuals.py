import matplotlib.pyplot as plt
import numpy as np

def plot_posterior(dice):
    """Plots the posterior probability distribution."""
    x = np.linspace(0, 1, 100)
    fig, ax = plt.subplots()

    for i, dist in enumerate(dice.get_posterior()):
        ax.plot(x, dist.pdf(x), label=f'Side {i+1}')

    ax.set_title("Posterior Distributions of Dice Fairness")
    ax.legend()
    plt.show()
