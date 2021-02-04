import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.001)

m = 3
a = 5
V_0 = 0
k = 1

def body_function(V, t):
    dmdt = a - ((V**2) * k)/m
    return dmdt

solve_Bi = odeint(body_function, V_0, t)

plt.plot(t, solve_Bi[:,0])
plt.xlabel('Время')
plt.ylabel('Скорость')
plt.title('Скорость тела')
plt.legend()

plt.show()
 
