import spiceypy as spice
import matplotlib.pyplot as plt
import numpy as np

spice.furnsh("kernels/de430.bsp")

et_start = spice.str2et("2025-01-01")
et_end = spice.str2et("2025-01-10")
et_array = np.linspace(et_start, et_end, 500)

positions = []
for et in et_array:
    pos, _ = spice.spkpos("MARS", et, "J2000", "LT+S", "EARTH")
    positions.append(pos)

positions = np.array(positions)

plt.figure(figsize=(8,6))
plt.plot(positions[:, 0], positions[:, 1])
plt.title("Mars Trajectory as Seen from Earth (X vs Y)")
plt.xlabel("X [km]")
plt.ylabel("Y [km]")
plt.grid(True)
plt.axis("equal")
plt.show()

spice.unload("kernels/de430.bsp")
