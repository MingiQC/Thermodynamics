from math import sqrt
from numpy import arange
from pylab import plot, show, xlabel, ylabel

def f(x,y):
    t=-y/(sqrt(x**2+1))+1/(x+sqrt(1+x**2))
    return t

#init. condit. y=0, x=0
x_i=0
y_i=0

x_f=10 #End of interval
N=1000
h=(x_f-x_i)/N
px=[]
py=[]

#EulerMethod y_{i+1}=y_{i}+h*f_{i}
px.append(x_i)
py.append(y_i)
x_list=arange(x_i,x_f,h)
y=y_i

for xx in x_list:
    y+=h*f(xx,y)
    py.append(y)
    px.append(xx+h)

plot(px,py)
xlabel(r'$x$', fontsize=20)
ylabel(r'$y$', fontsize=20)
show()
