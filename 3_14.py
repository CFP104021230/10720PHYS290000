"""
Angry bird game demo, Mar. 14, 2019.
Copyright @ Wei-Chih Huang (noctildon2@gmail.com)
"""

import numpy as np
import matplotlib.pylab as plot
import math
import random

# 重力+速度
g = 9.8


# generate x and y axis
def trajectory(velocity, theta):
    t = np.linspace(0, 100, num=50000)
    x1 = []
    y1 = []
    for k in t:
        x = ((velocity * k) * np.cos(theta))
        y = ((velocity * k) * np.sin(theta)) - ((0.5 * g) * (k**2))
        x1.append(x)
        y1.append(y)
    p = [i for i, j in enumerate(y1) if j < 0]
    for i in sorted(p, reverse=True):
        del x1[i]
        del y1[i]

    return [x1, y1]


def random_point(xlim, ylim):
    x = random.uniform(0, xlim)
    y = random.uniform(0, ylim)
    return [x, y]


# x,y are list, random_x, random_y are float
def isHit(x, y, random_x, random_y, scale=1):
    xHit = False
    yHit = False
    for _ in x:
        if abs(_ - random_x) <= scale:
            print('x:', _, random_x)
            xHit = True
            break
    for _ in y:
        if abs(_ - random_y) <= scale:
            print('y:', _, random_y)
            yHit = True
            break

    return xHit and yHit


# ratio = random.uniform(2, 10)
ratio = 6
random_x, random_y = random_point(100, 50)
x, y = trajectory(100, math.pi / ratio)

if isHit(x, y, random_x, random_y, 0.01):
    print('You hit it!')
else:
    print('Try again')

plot.plot(x, y)
plot.plot(random_x, random_y, 'ro')
plot.show()
