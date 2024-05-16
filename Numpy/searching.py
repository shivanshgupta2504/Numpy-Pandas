import numpy as np
import random

np1 = np.array([random.randint(1, 100) for _ in range(10)])
print(np1)
even_array_index = np.where(np1 % 2 == 0)
print(even_array_index[0])
print(np1[even_array_index[0]])

odd_array_index = np.where(np1 % 2 == 1)
print(odd_array_index[0])
print(np1[odd_array_index[0]])

