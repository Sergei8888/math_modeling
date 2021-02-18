import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

	
t = np.arange(-1, 1, 0.01)

def diff_func(a, t):
    x, y = a
    dx_dt= 3*x-2*y+ (np.exp(3*t))/(np.exp(t)+1)
    dy_dt = x - (np.exp(3*t))/(np.exp(t)+1)
    return dx_dt, dy_dt

x0=5
y0=-7
a0= x0, y0

sol = odeint(diff_func, a0, t)

plt.plot(t, sol[:, 1], 'b', label='a(t)')

plt.legend()
plt.show()