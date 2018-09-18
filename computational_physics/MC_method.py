from random import random, seed
from numpy import empty, linspace
from math import sqrt
from matplotlib import pyplot as plt

np=1000000 #number of random points
seed()
x=empty(np,float)
y=empty(np,float)
i=0
ncircle=0.0
while i<np:
    x[i]=random()
    y[i]=random()
    if (y[i]<sqrt(1.0-x[i]**2)):
        ncircle+=1.0
    i+=1

print("pi=", 4*ncircle/float(np))

#Plotting

np=1000
px=linspace(0,1,np)
py=empty(np, float)
i=0
for xx in px:
    py[i]=sqrt(1.0-xx**2)
    i+=1

plt.plot(x,y, 'g.', markersize=0.7)
plt.plot(px, py, linewidth=2)
ax=plt.gca()
ax.set_aspect('equal')

plt.show()
