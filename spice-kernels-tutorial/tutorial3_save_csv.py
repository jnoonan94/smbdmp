import spiceypy as spice
import numpy as np

spice.furnsh("kernels/de430.bsp")

et_start = spice.str2et("2025-01-01")
et_end = spice.str2et("2025-01-02")
ets = np.linspace(et_start, et_end, 100)
mars_positions = [spice.spkpos("MARS", et, "J2000", "LT+S", "EARTH")[0] for et in ets]

np.savetxt("mars_positions.csv", mars_positions, delimiter=",", header="X,Y,Z", comments="")
print("Saved Mars positions to 'mars_positions.csv'")

spice.unload("kernels/de430.bsp")
