#2014103332 김민기  
from math import pi, sin, cos
from numpy import linspace
from pylab import plot, show, xlim, ylim

def f(x):
    y=x**2
    return y

#Three point method

def df_dx(x0, xe, n):
    x=x0
    h=(xe-x0)/n
    xi=[]
    yi=[]
    for i in range(0,n):
        yi.append((f(x+h)-f(x-h))/(2*h))
        xi.append(x)
        x+=h
    plot(xi,yi,'ro')
    return(1)

#Plot Sin(x) d/dx Sin(x) (Cos(x))
Np=1000
px=linspace(-2.0,2.0,Np)
py=[]
dpy=[]
for xx in px:
    py.append(f(xx))
    dpy.append(2*xx)
plot(px,py)
plot(px,dpy,'k')

#Plot dy/dx
Ndx=100
df_dx(-2.0,2.0,Ndx)

ylim(-4.1,4.1)
xlim(-2, 2)



show()
        
