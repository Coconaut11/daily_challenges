#COMPLETED

from collections import namedtuple
import random
import math
struct = namedtuple

Dot = struct("dot", "x y")

def getPI(k, w=20, h=20):
    inside = 0
    for i in range(0, k):
        if dist(Dot(w/2, h/2), Dot(random.randrange(0, w), random.randrange(0, h))) < w/2:
            inside += 1
    
    print(inside)
    return (4*inside/k)

def dist(dot0, dot1):
    x = dot1.x-dot0.x
    y = dot1.y-dot0.y
    return abs(math.sqrt(x**2 + y**2))

print(getPI(10000000))