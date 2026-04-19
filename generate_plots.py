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
