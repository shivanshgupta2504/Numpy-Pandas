import numpy as np

# Numpy - Numeric Python
# Contains objects of same datatype
# ndarray - n-dimensional array

# Single dimension arrays
np1 = np.array([1, 2, 3])
print(np1)
print(np1.shape)

np2 = np.arange(10)
print(np2)

np3 = np.arange(0, 10, 2)
print(np3)

np4 = np.zeros(10)
print(np4)

# Multi-dimensional arrays
np5 = np.zeros((2, 10))
print(np5)

np6 = np.full((2, 10), 6)
print(np6)
print(np6.shape)

# Lists to numpy array
my_list = [1, 2, 3, 4]
np7 = np.array(my_list)
print(np7)
print(type(np7))
print(np7.shape)
