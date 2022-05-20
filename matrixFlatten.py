import numpy as np
from random import randint

n = randint(0, 9)
m = randint(0, 9)
p = randint(0, 9)

q = n * m * p

matrix3d = np.zeros((n, m, p))
matrix1d = np.zeros(q)

# Flatting the 3d matrix
for i in range(n):
    for j in range(m):
        for k in range(p):
            matrix3d[i, j, k] = randint(0, 99)
            matrix1d[j + i * m + k * n * m] = matrix3d[i, j, k]

# Testing out the flatting algorithm using random indecies

for i in range(n * m * p):
    i = randint(0, n - 1)
    j = randint(0, m - 1)
    k = randint(0, p - 1)
    if matrix1d[j + i * m + k * n * m] != matrix3d[i, j, k]:
        print("error at i, j, j = " + str(i) + " " + str(j) + " " + str(k))
print("matrix flatten done correctly")


