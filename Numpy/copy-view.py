import numpy as np

np1 = np.arange(10)
np2 = np.arange(10)

# View - creates a copy but that is still linked to original one
np3 = np1.view()
print(f"Original NP1 {np1}")
print(f"Original NP3 {np3}")
np1[0] = 21
print(f"Changed NP1 {np1}")
print(f"Original NP3 {np3}")

# Copy - creates a separate copy and both work independently
np4 = np2.copy()
print(f"Original NP2 {np2}")
print(f"Original NP4 {np4}")
np2[0] = 21
print(f"Changed NP2 {np2}")
print(f"Original NP4 {np4}")

