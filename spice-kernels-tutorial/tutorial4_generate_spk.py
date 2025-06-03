import numpy as np
import spiceypy as spice

mu = 398600.4418
radius = 7000
orbital_period = 2 * np.pi * np.sqrt(radius**3 / mu)

et0 = spice.str2et("2025-01-01T00:00:00")
times = np.linspace(0, orbital_period, 100)
ets = et0 + times

positions = []
velocities = []
for t in times:
    theta = 2 * np.pi * t / orbital_period
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    z = 0
    vx = -radius * np.sin(theta) * (2 * np.pi / orbital_period)
    vy = radius * np.cos(theta) * (2 * np.pi / orbital_period)
    vz = 0
    positions.append([x, y, z])
    velocities.append([vx, vy, vz])

data_lines = []
for i, et in enumerate(ets):
    line = f"{et:.6f} {positions[i][0]:.6f} {positions[i][1]:.6f} {positions[i][2]:.6f} {velocities[i][0]:.6f} {velocities[i][1]:.6f} {velocities[i][2]:.6f}"
    data_lines.append(line)

with open("example_spk20_data.txt", "w") as f:
    f.write("\n".join(data_lines))

print("Saved simulated orbit to example_spk20_data.txt")
