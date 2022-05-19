import numpy as np
from random import randint

n = randint(0, 9)
m = randint(0, 9)
p = randint(0, 9)

q = n * m * p

matrix3d = np.zeros((n, m, p))
matrix1d = np.zeros(q)
y = 0

for k in range(p):
    for j in range(m):
        for i in range(n):
            matrix3d[i, j, k] = randint(0, 99)
            matrix1d[y] = matrix3d[i, j, k]
            y += 1



# initialIdx
# 


for i in range(n):
    for j in range(m):
        for k in range(p):
            idx = i + j * n + k * n * m
            if matrix1d[idx] != matrix3d[i, j, k]:
                print("error at i, j, j = " + str(i) + " " + str(j) + " " + str(k))

