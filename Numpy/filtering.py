import numpy as np
import random

np1 = np.array([random.randint(1, 100) for _ in range(10)])
print(np1)

filtered1 = [i % 2 == 0 for i in np1]  # filter out even numbers
print(filtered1)
print(np1[filtered1])

filtered2 = np1 % 2 == 1  # filter out odd numbers
print(filtered2)
print(np1[filtered2])

