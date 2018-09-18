from math import pi, sin, cos
from numpy import linspace
from pylab import plot, show, xlim, ylim

def f(x):
    y=sin(x)
    return y

# forward difference(Two point) x+=h가 나중에나옴

def df_dx_forward(x0,xe,n):
    x=x0
    h=(xe-x0)/n
    xi=[]
    yi=[]
    for i in range(0,n):
        yi.append((f(x+h)-f(x))/h)
        xi.append(x)
        x+=h
    plot(xi,yi,'ro')
    return(1)

# backward difference(Two point) x+=h가 먼저나옴

def df_dx_backward(x0,xe,n):
    x=x0
    h=(xe-x0)/n
    xi=[]
    yi=[]
    for i in range(0,n):
        x+=h
        yi.append((f(x)-f(x-h))/h)
        xi.append(x)
    plot(xi,yi,'g+')
    return(1)

#Plot Sin(x) d/dx Sin(x) (Cos(x))
Np=1000
px=linspace(0,2*pi,Np)
py=[]
dpy=[]
for xx in px:
    py.append(f(xx))
    dpy.append(cos(xx))
plot(px,py)
plot(px,dpy)

#Plot fd&bd
Ndx=100
df_dx_forward(0,2+pi,Ndx)
df_dx_backward(0,2*pi,Ndx)

show()
        
