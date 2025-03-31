import matplotlib.pyplot as plt
import numpy as np

def plot_posterior(dice):
    """Plots the posterior probability distribution with fairness line, labels, and MAP estimates."""
    x = np.linspace(0, 1, 100)
    fig, ax = plt.subplots(figsize=(10, 6))
    max_mean = 0
    max_side = None

    for i, dist in enumerate(dice.get_posterior()):
        y = dist.pdf(x)
        ax.plot(x, y, label=f'Side {i+1}')

        # Plot MAP (mode) or mean if mode is not defined
        if dist.args[0] > 1 and dist.args[1] > 1:
            map_estimate = (dist.args[0] - 1) / (dist.args[0] + dist.args[1] - 2)
        else:
            map_estimate = dist.mean()

        ax.axvline(map_estimate, linestyle='--', alpha=0.3)

        if map_estimate > max_mean:
            max_mean = map_estimate
            max_side = i + 1

    # Draw fairness line at 1/6
    ax.axvline(1/6, color='gray', linestyle=':', label='Fair Probability (1/6)')

    # Add shaded area under the most probable side
    max_dist = dice.get_posterior()[max_side - 1]
    ax.fill_between(x, max_dist.pdf(x), alpha=0.2, label=f'Most likely: Side {max_side}')

    ax.set_title("Posterior Distributions of Dice Fairness")
    ax.set_xlabel("Probability of Each Side")
    ax.set_ylabel("Density")
    ax.legend()
    plt.grid(True)
    plt.show()
