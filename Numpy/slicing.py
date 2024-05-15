# Slicing in numpy arrays works in same way as list slicing
import numpy as np

np1 = np.arange(20)  # [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# Slicing
print(np1[2:6])
# Slicing till end
print(np1[8:])
# Slicing till an index
print(np1[:13])
# Negative Slicing
print(np1[-3:-1])
# Steps
print(np1[5:17:2])
print(np1[::2])
print(np1[::-1])

# Slicing 2D Array
np2 = np.array(
    [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    ]
)
print(np2)
print(np2.shape)
print(np2[1, 4])  # similar to np2[1][4]
print(np2[0:, 2:6])

