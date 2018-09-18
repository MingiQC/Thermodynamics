from math import sin
from numpy import arange
from pylab import plot, xlabel, ylabel, show

def f(x,t):
    y=-x**3 + sin(t)
    return y

#initial condition
t_i = 0.0
x_i = 0.0

t_f = 10.0  # End of the interval to calculate

N=1000  #number of steps
h=(t_f-t_i)/N
pt=[]
px=[]

pt.append(t_i)
px.append(x_i)
t_list=arange(t_i, t_f, h)
x=x_i
for t in t_list:
    x+=h*f(x,t)
    px.append(x)
    pt.append(t+h)

plot(pt, px)
xlabel(r"$t$", fontsize=20)
ylabel(r"$x(t)$", fontsize=20)
show()
