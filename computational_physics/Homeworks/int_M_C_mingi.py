#2014103332김민기 
from random import random, seed
np=100000
seed()
i=0
inte=0
xi, xf = 0, 1
yi, yf = 0, 1
zi, zf = 0, 1
while i<np:
    x=xf*random()
    y=yf*random()
    z=zf*random()
    inte+=(x+y+z)
    i+=1

print('Int((x+y+z),{x,%s,%s},{y,%s,%s},{z,%s,%s})='
      %(xi, xf, yi, yf, zi, zf), inte*(xf-xi)*(yf-yi)*(zf-zi)/np)
