import numpy as np

def generate_data(seed):
    """
    Generate synthetic timestamps and two temperature sensor arrays.

    Parameters
    ----------
    seed : int or None
        Seed for numpy.random.default_rng. If None, a non-deterministic generator is used.

    Returns
    -------
    timestamps : ndarray, shape (200,), dtype float64
        Evenly spaced timestamps from 0.0 to 10.0 seconds inclusive.
    sensor_a : ndarray, shape (200,), dtype float64
        Synthetic temperature readings (degrees Celsius) for sensor A (normal mean=25, std=3).
    sensor_b : ndarray, shape (200,), dtype float64
        Synthetic temperature readings (degrees Celsius) for sensor B (normal mean=27, std=4.5).
    """
    rng = np.random.default_rng(seed)
    timestamps = np.linspace(0.0, 10.0, 200, dtype=np.float64)
    sensor_a = rng.normal(25.0, 3.0, size=200).astype(np.float64)
    sensor_b = rng.normal(27.0, 4.5, size=200).astype(np.float64)
    return timestamps, sensor_a, sensor_b


if __name__ == "__main__":
    ts, a, b = generate_data(1234)
    print(ts.shape, a.shape, b.shape)


def plot_scatter(ax, timestamps, sensor_a, sensor_b, *, s=30, cmap='viridis', alpha=0.8):
    """
    Draw a scatter plot of two temperature sensors onto an existing Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to modify in place.
    timestamps : array_like, shape (N,)
        Time values corresponding to measurements (used for color mapping).
    sensor_a : array_like, shape (N,)
        Temperature readings from sensor A (°C).
    sensor_b : array_like, shape (N,)
        Temperature readings from sensor B (°C).
    s : int, optional
        Marker size for the scatter points (default: 30).
    cmap : str or Colormap, optional
        Colormap for coloring points by timestamp (default: 'viridis').
    alpha : float, optional
        Marker transparency (default: 0.8).

    Returns
    -------
    None
        The function updates the provided Axes in place and returns None.
    """
    import matplotlib.pyplot as _plt

    timestamps = np.asarray(timestamps)
    sensor_a = np.asarray(sensor_a)
    sensor_b = np.asarray(sensor_b)

    sc = ax.scatter(sensor_a, sensor_b, c=timestamps, cmap=cmap, s=s, alpha=alpha)
    _plt.colorbar(sc, ax=ax, label='Time (s)')
    ax.set_xlabel('Sensor A (°C)')
    ax.set_ylabel('Sensor B (°C)')
    ax.set_title('Sensor A vs Sensor B (colored by time)')
    ax.grid(True, linestyle='--', alpha=0.6)


def plot_histogram(ax, sensor_a, sensor_b, bins=30, density=False, alpha=0.6, colors=("C0", "C1")):
    """
    Draw overlaid histograms for two temperature sensors onto an existing Axes.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Matplotlib Axes object to modify in place.
    sensor_a : array_like, shape (N,)
        Temperature readings from sensor A (°C).
    sensor_b : array_like, shape (N,)
        Temperature readings from sensor B (°C).
    bins : int or sequence, optional
        Number of bins or explicit bin edges for the histograms (default: 30).
    density : bool, optional
        If True, plot probability density instead of counts (default: False).
    alpha : float, optional
        Transparency for the histogram bars (default: 0.6).
    colors : tuple of str, optional
        Colors for sensor A and sensor B (default: ("C0", "C1")).

    Returns
    -------
    None
        Updates the provided Axes in place and returns None.
    """
    sensor_a = np.asarray(sensor_a)
    sensor_b = np.asarray(sensor_b)

    # Determine bin edges when an integer is provided
    if isinstance(bins, int):
        vmin = min(sensor_a.min(), sensor_b.min()) - 1.0
        vmax = max(sensor_a.max(), sensor_b.max()) + 1.0
        bins = np.linspace(vmin, vmax, bins)

    ax.hist(sensor_a, bins=bins, alpha=alpha, label="Sensor A", color=colors[0], density=density)
    ax.hist(sensor_b, bins=bins, alpha=alpha, label="Sensor B", color=colors[1], density=density)

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Density" if density else "Count")
    ax.set_title("Histogram of Sensor Temperatures")
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.5)


def main(seed=1234, show=True, save=True):
    """
    Generate synthetic data and produce example scatter and histogram plots.

    Parameters
    ----------
    seed : int or None, optional
        Seed passed to generate_data for reproducibility (default=1234).
    show : bool, optional
        If True, display the figures with plt.show() (default=True).
    save : bool, optional
        If True, save the combined figure to 'sensor_plots.png' (default=True).

    Returns
    -------
    None
        Generates and optionally shows/saves the figures. The function modifies
        matplotlib state but does not return values.
    """
    import matplotlib.pyplot as plt

    # Generate data
    timestamps, sensor_a, sensor_b = generate_data(seed)

    # Create side-by-side plots: scatter (left) and histogram (right)
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Left: scatter colored by time
    plot_scatter(axes[0], timestamps, sensor_a, sensor_b)

    # Right: overlaid histograms
    plot_histogram(axes[1], sensor_a, sensor_b, bins=30, density=False)

    plt.tight_layout()

    if save:
        fig.savefig('sensor_plots.png', dpi=150)

    if show:
        plt.show()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Generate example sensor plots')
    parser.add_argument('--seed', type=int, default=1234, help='RNG seed (default: 1234)')
    parser.add_argument('--no-show', dest='show', action='store_false', help='Do not call plt.show()')
    parser.add_argument('--no-save', dest='save', action='store_false', help='Do not save the figure')
    parser.set_defaults(show=True, save=True)
    args = parser.parse_args()

    main(seed=args.seed, show=args.show, save=args.save)
