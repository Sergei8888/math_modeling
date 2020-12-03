import matplotlib.pyplot as plt
import numpy as np
a = 1
b = 1
c = 0
k = 2
x = np.arange(-10, 10, 0.01)
y = a*x**2 + b*x + c
plt.plot(x, y) #[x][y]
plt.show()
y = k/x
y = np.ma.masked_less(y, -10)
y = np.ma.masked_greater(y, 10)

plt.plot(x, y)
plt.show()

