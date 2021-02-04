import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10, 0.00001)

k = 2 #Бактерии делятся на 2
n_0 = 1 #Начальное количество бактерий

def bio_function(n, t):
    dmdt = k * n
    return dmdt

solve_Bi = odeint(bio_function, n_0, t)

plt.plot(t, solve_Bi[:,0])
plt.xlabel('Время')
plt.ylabel('Кол-во бактерий')
plt.title('Размножение бактерий')
plt.legend()

plt.show()
 

