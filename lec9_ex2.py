import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 48, 1)
n_0 = 1000
k = 0.08

def invest_function(n, t):
    dmdt = -k * n * t
    return dmdt

solve_Bi = odeint(invest_function, n_0, t)

plt.plot(t, solve_Bi[:,0])
plt.xlabel('Время')
plt.ylabel('Кол-во инвестиций')
plt.title('Инвестиции')
plt.legend()

plt.show()
 
