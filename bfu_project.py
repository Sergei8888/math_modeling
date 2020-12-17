import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

figure, axes = plt.subplots()

plt.xlim(-20, 20)
plt.ylim(-20, 20)
axes.set_aspect(1)

circleCenter = [0, 10]
circleRadius = 2
circleVerticalVelocity = 0
circleHorizontalVelocity = 0
circleHorizontalAcceleration = 1
circleVerticalAcceleration = 1
g = 10

draw_circle = plt.Circle((circleCenter[0], circleCenter[1]), circleRadius)

def init():
    axes.add_patch(draw_circle)
    return draw_circle,

def animate(i):
    global circleCenter, circleRadius, circleVerticalVelocity, circleHorizontalVelocity

    if 20 - circleCenter[0] <= 3 or  20 - circleCenter[0] >=37:
        circleHorizontalVelocity*= -1
    if 20 - circleCenter[1] <= 3 or  20 - circleCenter[1] >=37:
        circleVerticalVelocity*= -1
    
    '''circleVerticalVelocity -= 0.04 
    if 20 - circleCenter[1] <= 3:
        circleVerticalVelocity = 0'''

    circleHorizontalVelocity *= circleHorizontalAcceleration
    circleVerticalVelocity *= circleVerticalAcceleration

    circleCenter[0] = circleCenter[0] + circleHorizontalVelocity
    circleCenter[1] = circleCenter[1] + circleVerticalVelocity

    draw_circle.center = (circleCenter[0], circleCenter[1])
    return draw_circle,

anim = FuncAnimation(figure, animate, 
                               init_func=init,
                               interval=10,
                               blit=True)


plt.title('Circle')
plt.show()

