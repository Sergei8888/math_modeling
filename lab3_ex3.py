import numpy as np
import random

x_0 = random.randint(1, 50)
y_0 = random.randint(1, 50)
v = random.randint(1, 50)

txy = np.zeros([6, 3])

for i in range(0, 6):
    txy[i][0] = i
    txy[i][1] = x_0 + v*i
    txy[i][2] = y_0 + v*i - (9.8*i**2)/2
print(txy)


