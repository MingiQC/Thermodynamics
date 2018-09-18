from math import sin
from numpy import arange
from pylab import plot, xlabel, ylabel, show

def f(x,t):
    y=-x**3+sin(t)
    return y

#init. condit.
t_i, x_i = 0.0, 0.0

t_f=10.0 # End of the interval to calculate
N=1000
h=(t_f-t_i)/N
pt=[]
px=[]
pex=[]

pt.append(t_i)
px.append(x_i)
pex.append(x_i)
t_list=arange(t_i, t_f, h)
x=x_i
ex=x_i

for t in t_list:
    p=x+h*f(x,t) #predictor
    x+=0.5*h*(f(x,t)+f(p,t+h)) #corrector; x_{i+1}=x_{i}+h/2 (f_{i}+f(p,t))
    ex+=h*f(ex,t) # in case of euler method
    pex.append(ex)
    px.append(x)
    pt.append(t+h)

print("오일러 메서드와 PC메서드를 비교하려면 확대!")
plot(pt,px)
plot(pt,pex)
show()
