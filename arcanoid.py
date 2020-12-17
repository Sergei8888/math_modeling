import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

figure, axes = plt.subplots()

figLimits = 20 #

plt.xlim(0, figLimits)
plt.ylim(0, figLimits)
axes.set_aspect(1)

circleCenter = [figLimits/2, figLimits/2]
circleRadius = 1
circleVelocity = [0.11, 0.1]
circleAcceleration = [1, 1]

g = 10

draw_circle = plt.Circle((circleCenter[0], circleCenter[1]), circleRadius)

def init():
    axes.add_patch(draw_circle)
    return draw_circle,

def animate(i):
    global circleCenter, circleRadius, circleVelocity, circleAcceleration
    
    if circleCenter[0] <= 2 or circleCenter[0] >= 18:
        circleVelocity[0] *= -1
    if circleCenter[1] <= 2 or circleCenter[1] >= 18:
        circleVelocity[1] *= -1
        
    
    
    circleVelocity[1] = circleVelocity[1] - 0.01
    
    circleVelocity[0] *= circleAcceleration[0]
    circleVelocity[1] *= circleAcceleration[1]
    
    circleCenter[0] = circleCenter[0] + circleVelocity[0]
    circleCenter[1] = circleCenter[1] + circleVelocity[1]
    
    if circleCenter[0] < circleRadius:
        circleVelocity[0] = 0
        circleCenter[0] = circleRadius
    if circleCenter[1] < circleRadius:
        circleVelocity[1] = 0
        circleCenter[1] = circleRadius

    draw_circle.center = (circleCenter[0], circleCenter[1])
    
    return draw_circle,

anim = FuncAnimation(figure, animate, 
                               init_func=init,
                               interval=10,
                               blit=True)


plt.title('Circle')
plt.show()