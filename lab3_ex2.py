import constants
import numpy as np
import math

A = constants.g*100*(np.tan(np.radians(30))**2)
B = 2 * (np.cos(math.pi/3)**2)*(1-np.tan(np.radians(30))*np.tan(math.pi/3))
N = (2/np.sqrt(numpy.pi)) * (constants.h/(constants.k*200)**3/2) * constants.e**(-(constants.e)/((constants.k)*200))
print(np.sqrt(A/B))
print(N)
