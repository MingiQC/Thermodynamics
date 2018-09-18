from math import sin
from numpy import arange, array
from pylab import plot, xlabel, ylabel, show

#x'(t)=xy-x, y'(t)=y-xy+(sin(wt))^2

def f(r,t):
    x=r[0]
    y=r[1]
    fx=x*y-x
    fy=y-x*y+sin(t)**2
    return array([fx,fy],float)

#init. condit.
t_i, t_f = 0.0, 10.0
x_i, y_i = 1.0, 1.0

N=1000 #number of steps
h=(t_f-t_i)/N
pt=[]
px=[]
py=[]

pt.append(t_i)
px.append(x_i)
py.append(y_i)
t_list=arange(t_i, t_f, h)
x=x_i

r=array([x_i, y_i], float)

for t in t_list:
    k1=h*f(r,t)
    k2=h*f(r+0.5*k1, t+0.5*h)
    k3=h*f(r+0.5*k2, t+0.5*h)
    k4=h*f(r+k3, t+h)
    r+=(k1+2*k2+2*k3+k4)/6
    px.append(r[0])
    py.append(r[1])
    pt.append(t+h)

plot(pt,px, 'r')
plot(pt,py, 'b')
xlabel(r'$t$', fontsize=20)
ylabel(r'$x(t)$, $y(t)$', fontsize=20)
show()

plot(px,py)
show()
