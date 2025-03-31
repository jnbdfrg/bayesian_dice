import matplotlib.pyplot as plt
import numpy as np


def plot_posterior(dice):
    """
    Posterior plot showing fairness reference and most likely side only,
    with side summaries in a legend box.
    """
    x = np.linspace(0, 1, 100)
    fig, ax = plt.subplots(figsize=(10, 6))

    posteriors = dice.get_posterior()
    map_estimates = []
    side_summaries = []  # store interpretation text
    total_rolls = int(sum([a - 1 for a in dice.alpha]))

    for i, dist in enumerate(posteriors):
        y = dist.pdf(x)
        ax.plot(x, y, label=f'Side {i+1}')

        # Compute MAP or fallback to mean
        if dist.args[0] > 1 and dist.args[1] > 1:
            map_est = (dist.args[0] - 1) / (dist.args[0] + dist.args[1] - 2)
        else:
            map_est = dist.mean()

        map_estimates.append((i + 1, map_est, dist))

    # Find most likely side
    max_side, max_map, max_dist = max(map_estimates, key=lambda x: x[1])

    # Shade only the most likely side’s posterior
    ax.fill_between(x, max_dist.pdf(x), alpha=0.2, label=f'Most likely: Side {max_side}')

    # Add text box with summary
    summary_text = "\n".join(side_summaries)
    props = dict(boxstyle='round', facecolor='white', alpha=0.9)
    ax.text(1.05, 0.5, summary_text, transform=ax.transAxes,
            fontsize=10, verticalalignment='center', bbox=props)

    ax.set_title("Posterior Distributions of Dice Fairness")
    ax.set_xlabel("Probability of Each Side")
    ax.set_ylabel("Density")
    ax.legend(loc='upper left')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
