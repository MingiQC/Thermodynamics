from math import tanh, cosh
from numpy import linspace
from pylab import plot, show, xlabel, ylabel

accuracy=1e-12

def arctanh(u):
    x=0.0
    delta=1.0
    while abs(delta)>accuracy:
        delta=(tanh(x)-u)*cosh(x)**2
        x-=delta
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
plot(pu,px2)
ylabel(r'$\tanh^{-1} u$', fontsize=18)
xlabel(r'$u$', fontsize=18)
show()
