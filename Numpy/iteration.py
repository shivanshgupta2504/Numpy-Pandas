import numpy as np

# Iteration using for loops
np1 = np.arange(10)
for i in np1:
    print(i)

np2 = np1.reshape(2, 5)
for i in np2:
    print(i)  # rows
    for j in i:
        print(j)  # each element

print()
np3 = np.arange(12).reshape(2, 3, 2)
print(np3, "\n")
for i in np3:
    print(i, "\n")
    for j in i:
        print(j, "\n")
        for k in j:
            print(k)

# Iteration using np.nditer()
for i in np.nditer(np3):
    print(i)
