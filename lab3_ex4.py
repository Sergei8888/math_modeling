import numpy as np
import random

N = random.randint(1, 50)
M = random.randint(1, 50)

mass = np.zeros([N, M])

for i in range(N):
    for j in range(M):
        mass[i][j] = np.sin(N * (i+1) + M * (j+1))

print(mass)


