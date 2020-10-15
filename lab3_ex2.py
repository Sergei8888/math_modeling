import constants
import numpy as np
import math

A = constants.g*100*(np.tan(np.radians(30))**2)
B = 2 * (np.cos(math.pi/3)**2)*(1-np.tan(np.radians(30))*np.tan(math.pi/3))
print(np.sqrt(A/B))
