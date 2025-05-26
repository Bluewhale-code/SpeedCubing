from vpython import *


t = 0.01
s = 1.99  
wall1 = box(pos=vector(-1 - t/2, 0, 0), size=vector(t, s, s), color=color.green)
wall2 = box(pos=vector(1 + t/2, 0, 0), size=vector(t, s, s), color=color.blue)
wall3 = box(pos=vector(0, 0, 1 + t/2), size=vector(s, s, t), color=color.red)
wall4 = box(pos=vector(0, 0, -1 - t/2), size=vector(s, s, t), color=color.yellow)
floor = box(pos=vector(0, -1 - t/2, 0), size=vector(s, t, s), color=color.orange)
ceiling = box(pos=vector(0, 1 + t/2, 0), size=vector(s, t, s), color=color.white)



for i in range(120):
    rate(60)
   
