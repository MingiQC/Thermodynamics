from math import sin, pi
from numpy import linspace

def f(x):
    y=sin(x)
    return y

def simpson13(x0, xe, num_int):
    x=linspace(x0, xe, num_int)
    h=x[1]-x[0]
    i=0
    integral=0.0
    i_max=x.size-2
    while i<i_max:
        integral+=(f(x[i])+4*f(x[i+1])+f(x[i+2]))
        i+=2
    return(integral*h/3)

def simpson38(x0, xe, num_int):
    x=linspace(x0, xe, num_int)
    h=x[1]-x[0]
    i=0
    integral=0.0
    i_max=x.size-3
    while i<i_max:
        integral+=(f(x[i])+3*f(x[i+1])+3*f(x[i+2])+f(x[i+3]))
        i+=3
    return(integral*h*3/8)

integ1 = simpson13(0.0, pi, 1000)
integ2 = simpson38(0.0, pi, 999)
print('Simpson 1/3 result: ', integ1)
print('Simpson 3/8 result: ', integ2)
