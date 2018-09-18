from math import sin
from numpy import arange
from pylab import plot, xlabel, ylabel, show

def f(x,t):
    y=-x**3+sin(t)
    return y

#init. condit.
t_i, x_i = 0.0, 0.0

t_f = 10.0

N=1000
h=(t_f-t_i)/N
pt=[]
px=[]
pt.append(t_i)
px.append(x_i)
t_list=arange(t_i, t_f, h)
x=x_i
for t in t_list:
    k1=h*f(x,t)
    k2=h*f(x+0.5*k1, t+0.5*h)
    x+=k2
    px.append(x)
    pt.append(t+h)

plot(pt,px)
show()
