import numpy as np

# 1-D array
np1 = np.arange(stop=12)
print(np1)
print(np1.shape)

# 2-D array
np2 = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
print(np2)
print(np2.shape)

# reshape to 2-D
np3 = np1.reshape(3, 4)
print(np3)
print(np3.shape)

# reshape to 3-D
np4 = np1.reshape(2, 3, 2)
print(np4)
print(np4.shape)

# Flatten to 1-D array
np5 = np2.reshape(-1)
print(np5)
print(np5.shape)

