# SPICE Kernels Tutorial for Aspiring Flight Controllers

This repository contains four beginner-friendly Python tutorials on working with NASA NAIF SPICE kernels. Designed for students and interns interested in mission ops and flight control.

## Tutorials
- **Tutorial 1**: Load and visualize planetary positions from SPICE kernels.
- **Tutorial 2**: Manipulate and transform position data using SPICE APIs.
- **Tutorial 3**: Save ephemeris data to CSV.
- **Tutorial 4**: Simulate and create your own SPK kernel using NAIF tools.

## Setup
```bash
pip install -r requirements.txt
```

Place the following NAIF kernels in the `kernels/` folder:
- `de430.bsp` (planet ephemerides)
- `naif0012.tls` (leap seconds)

## Notes
- NAIF Toolkit binaries (`spk20a`, `spkmerge`) must be installed and available on your system PATH.
- Tutorials assume a basic Python environment with matplotlib and numpy.
