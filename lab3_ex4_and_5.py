import numpy as np
import random as rnd
import pandas as pd

N = rnd.randint(1, 11)
M = 2

mass = np.zeros([N, M])

for i in range(N):
    for j in range(M):
        elem = np.sin(N * (i+1) + M * (j+1))
        if elem > 0:
            mass[i][j] = elem
        else:
            mass[i][j] = 0
print(mass)
print("")

for i in range(N):
    for j in range(M):
        if j == 0:
            x = mass[i][j]
            mass[i][j] = mass[i][j+1]
            mass[i][j+1] = x
print(mass)