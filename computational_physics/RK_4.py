from numpy import arange
from math import sin
from pylab import plot, show

#4th order runge-kutta method
# y(t+h)=y(t)+1/6 (c1+2c2+2c3+c4)
# c1 = h f(y,t)
# c2 = h f(y+c1/2 , t+h/2)
# c3 = h f(y+c2/2 , t+h/2)
# c4 = h f(y+c3 , t+h)

def f(x,t):
    y= -x**3 + sin(t)
    return y

#init. condit.
t_i, x_i = 0.0 , 0.0

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
    k3=h*f(x+0.5*k2, t+0.5*h)
    k4=h*f(x+k3, t+h)
    x+=(k1+2*k2+2*k3+k4)/6
    px.append(x)
    pt.append(t+h)

plot(pt,px)
show()
