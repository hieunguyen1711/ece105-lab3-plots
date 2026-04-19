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
