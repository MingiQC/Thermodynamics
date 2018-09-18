from math import sin
from numpy import arange
from pylab import plot, xlabel, ylabel, show

def f(x,t):
    y=-x**3+sin(t)
    return y

#init. condit.
t_i=0.0
x_i=0.0

t_f=10.0  # End of the interval to calculate
N=1000
h=(t_f-t_i)/N
pt=[]
px=[]
#Euler method: x_{i+1}=x_{i}+hf_{i}, x_{i+1}=x(t+h)

pt.append(t_i)
px.append(x_i)
t_list=arange(t_i, t_f, h) #t_i 부터 t_f 까지 h간격으로 배열하기
x=x_i

for t in t_list:
    x+=h*f(x,t)  #x_{i+1}=x_{i}+h*f
    px.append(x)  
    pt.append(t+h) #t...t+h...t+2h....

plot(pt,px)
show()

#오일러메서드는 오차가 크다..
