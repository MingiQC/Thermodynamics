from math import tanh, cosh
from numpy import linspace
from pylab import plot, show, xlabel, ylabel

accuracy=1e-12

def f(x,u):
    y=tanh(x)-u
    return y

def arctanh(u):
    x1=0.0
    x2=0.1
    delta=1.0
    while abs(delta)>accuracy:
        delta=f(x2,u)*(x2-x1)/(f(x2,u)-f(x1,u))
        x=x2-delta
        x1, x2 = x2, x
    return x

# d/dx(tanh_x) = 1/(cosh2_x). By nrm method, delta=-f/f'
# x=arctanh_u, u=tanh_x.
#find a root of tanh_x-u=0
#delta=-(tanh_x-u)/(tanh_x-u)'=-(tanh_x-u)cosh2_x

pu=linspace(-0.99,0.99,100)
px1=[]
px2=[]

for uu in pu:
    px1.append(arctanh(uu))
    px2.append(tanh(uu))
plot(pu,px1)
ylabel(r'$\tanh^{-1} u$', fontsize=18)
xlabel(r'$u$', fontsize=18)
show()
