from vpython import *

cube1 = box(pos=vector(0, 0, 0), size=vector(1,1,1), color=color.blue)
cube2 = box(pos=vector(0, 1, 0), size=vector(1,1,1), color=color.green)
cube3 = box(pos=vector(0, 2, 0), size=vector(1,1,1), color=color.red)
cube4 = box(pos=vector(0, 3, 0), size=vector(1,1,1), color=color.white)
cube5 = box(pos=vector(0, 4, 0), size=vector(1,1,1), color=color.orange)
for i in range(120):
    rate(60) 