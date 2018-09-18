from math import sqrt
from numpy import arange
from pylab import plot, xlabel, ylabel, show

def f(x,y):
    t=-y/sqrt(x**2+1)+sqrt(x**2+1)-x
    return t

#initial condition
y_i = 0.0
x_i = 0.0

y_f = 10.0  # End of the interval to calculate

N=1000  #number of steps
h=(y_f-y_i)/N
py=[]
px=[]

py.append(y_i)
px.append(x_i)
y_list=arange(y_i, y_f, h)
x=x_i
for y in y_list:
    x+=h*f(x,y)
    px.append(x)
    py.append(y+h)

plot(py, px)
xlabel(r"$y$", fontsize=20)
ylabel(r"$x(y)$", fontsize=20)
show()

plot(px,py)
xlabel(r'$x$', fontsize=20)
ylabel(r'$y(x)$', fontsize=20)
show()
