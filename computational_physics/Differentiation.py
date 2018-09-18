from numpy import linspace
from pylab import plot, show, xlim, ylim

#function

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
    plot(xi,yi,'ro',markersize=3)
    return(1)

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
    plot(xi,yi,'bs',markersize=2)
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
    plot(xi,yi,'g^',markersize=2)
    return(1)

#Plot
np=1000
px=linspace(-2,2,np)
py=[]
dpy=[]
for xx in px:
    py.append(f(xx))
    dpy.append(2*xx)
plot(px,py)
plot(px,dpy)

#Fd, Bd, TPd
ndx=100

df_dx_forward(-2,2,ndx)
df_dx_backward(-2,2,ndx)
df_dx(-2,2,ndx)

show()
