from vpython import *


cube = box(pos=vector(0, 0, 0), size=vector(2, 2, 2), color=color.cyan)

for i in range(120):
    rate(60)
    cube.rotate(angle=0.01, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
