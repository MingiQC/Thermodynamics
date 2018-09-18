from random import random, seed
from math import sin, pi

np=100000
seed()
i=0
inte=0.0
xi=0.0
xf=pi
while i<np:
    x=pi*random() # 0에서 pi까지 random number generating
    inte+=sin(x)
    i+=1

print('Int(sin(x),{x,0,pi})=', inte*(xf-xi)/np)
