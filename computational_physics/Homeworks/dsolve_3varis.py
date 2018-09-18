#2014103332 김민기 
from numpy import arange, array
from pylab import plot, xlabel, ylabel, show

#x'(t)=sigma(y-x), y'(t)=rx-y-xz, z'(t)=xy-bz

#constants...
sigma=10
r=28
b=8/3

def f(r,t):
    x=r[0]
    y=r[1]
    z=r[2]
    fx=10*(y-x)
    fy=28*x-y-x*z
    fz=x*y-8/3*z
    return array([fx,fy,fz],float)

#init. condit.
t_i, t_f = 0.0, 50.0
x_i, y_i, z_i = 0.0, 1.0, 0.0

N=1000 #number of steps
h=(t_f-t_i)/N
pt=[]
px=[]
py=[]
pz=[]

pt.append(t_i)
px.append(x_i)
py.append(y_i)
pz.append(z_i)
t_list=arange(t_i, t_f, h)

r=array([x_i,y_i,z_i], float)

for t in t_list:
    k1=h*f(r,t)
    k2=h*f(r+0.5*k1, t+0.5*h)
    k3=h*f(r+0.5*k2, t+0.5*h)
    k4=h*f(r+k3, t+h)
    r+=(k1+2*k2+2*k3+k4)/6
    px.append(r[0])
    py.append(r[1])
    pz.append(r[2])
    pt.append(t+h)

plot(pt,py, 'y')
plot(pt,px, 'r')
plot(pt,pz, 'b')
xlabel(r'$t$', fontsize=20)
ylabel(r'$x(t)$, $y(t)$, $z(t)$', fontsize=20)
show()

plot(px,pz, 'g')
xlabel(r'$X$')
ylabel(r'$Z$')
show()

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

# Prepare arrays px, py, pz

ax.plot(px, py, pz, label='curve')
ax.legend()
ax.set_xlabel('$X$',fontsize=20)
ax.set_ylabel('$Y$',fontsize=20)
ax.set_zlabel('$Z$',fontsize=20)
plt.show()
