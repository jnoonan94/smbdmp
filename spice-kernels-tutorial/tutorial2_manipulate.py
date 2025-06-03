import spiceypy as spice
import numpy as np

spice.furnsh("kernels/de430.bsp")

et = spice.str2et("2025-01-01T12:00:00")
pos, lt = spice.spkpos("MARS", et, "J2000", "LT+S", "EARTH")

r = np.linalg.norm(pos)
lon = np.arctan2(pos[1], pos[0])
lat = np.arcsin(pos[2]/r)

print(f"Distance to Mars: {r:.2f} km")
print(f"Longitude: {np.degrees(lon):.2f}°")
print(f"Latitude: {np.degrees(lat):.2f}°")

matrix = spice.pxform("J2000", "IAU_MARS", et)
mars_in_iau = matrix @ pos
print("Position of Mars in IAU_MARS frame:", mars_in_iau)

spice.unload("kernels/de430.bsp")
