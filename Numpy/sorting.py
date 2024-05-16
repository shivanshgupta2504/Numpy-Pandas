import numpy as np
import random

# np.sort() - returns a copy, doesn't change original
np1 = np.array([random.randint(1, 100) for _ in range(10)])
print(np1)
print(np.sort(np1))
print(np1)

np2 = np.array(["john", "tina", "zed", "aron", "shiv"])
print(np2)
print(np.sort(np2))

# In 2-D each row is sorted internally
np3 = np.array([random.randint(1, 100) for _ in range(12)]).reshape(3, 4)
print(np3)
print(np.sort(np3))

