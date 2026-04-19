# Synthetic Sensor Plots

## Summary
This repository contains a small Python script (generate_plots.py) to generate synthetic temperature sensor data and produce example plots (scatter and histogram). The script is intended as a standalone equivalent of the lab Jupyter notebook.

## Requirements
- Python 3.8+ (or compatible)
- Conda environment named `ece105` (recommended)
- Packages: numpy, matplotlib

## Installation
1. Activate the course environment:

n   conda activate ece105

2. Install dependencies (choose one):

   conda install -c conda-forge numpy matplotlib
   # or, if you prefer mamba:
   mamba install -c conda-forge numpy matplotlib

## Usage
Run the script to generate synthetic data and example plots:

python generate_plots.py

Options:
- `--seed <int>` : set RNG seed for reproducible data (default: 1234)
- `--no-show` : do not display the figure interactively
- `--no-save` : do not save the output image

## What the script does
- `generate_data(seed)` creates three numpy arrays:
  - `timestamps` (shape (200,)) — linearly spaced times from 0 to 10 s
  - `sensor_a` (shape (200,)) — synthetic temperatures (°C), N(25, 3)
  - `sensor_b` (shape (200,)) — synthetic temperatures (°C), N(27, 4.5)

- `plot_scatter(ax, timestamps, sensor_a, sensor_b)` draws a scatter of sensor_a vs sensor_b colored by time.
- `plot_histogram(ax, sensor_a, sensor_b)` draws overlaid histograms of the two sensors.
- `main()` generates data, produces side-by-side scatter + histogram, saves `sensor_plots.png` (by default), and optionally shows the figure.

## Output files
- `sensor_plots.png` — produced by default when running the script; a 2-panel figure (scatter and histogram) saved in the repository root.

## AI tools used and disclosure
This project used AI-assisted code generation. [Placeholder — describe the AI tools used, prompts, and what was accepted/modified.]

## License
(If applicable) Add license information here.
