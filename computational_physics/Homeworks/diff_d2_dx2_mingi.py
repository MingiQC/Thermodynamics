#2014103332 김민기 

from numpy import linspace
from pylab import plot, show, xlim, ylim, bar

def f(x):
    y=x**2
    return y

def d2f_dx2(x0, xe, n):
    x=x0
    h=(xe-x0)/n
    xi=[]
    yi=[]
    for i in range(0, n):
        yi.append((f(x+h)-2*f(x)+f(x-h))/(h**2))
        xi.append(x)
        x+=h
    plot(xi,yi,'ro')
    return()
#plot sine

Np=1000
px=linspace(-2,2, Np)
py=[]
for xx in px:
    py.append(f(xx))
plot(px,py)

#plot d2f/dx2
Ndx=100
d2f_dx2(-2,2, Ndx)

ylim(0, 3)
xlim(-2, 2)
show()
