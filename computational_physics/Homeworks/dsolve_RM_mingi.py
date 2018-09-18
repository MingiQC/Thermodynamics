#2014103332 김민기
from math import sqrt
from numpy import arange
from pylab import plot, show

#4th order runge-kutta method
# y(t+h)=y(t)+1/6 (c1+2c2+2c3+c4)
# c1 = h f(y,t)
# c2 = h f(y+c1/2 , t+h/2)
# c3 = h f(y+c2/2 , t+h/2)
# c4 = h f(y+c3 , t+h)

#2nd order runge_kutta method
# y(t+h)=y(t)+1/2 (c1+c2) 
# c1 = h f(y,t)
# c2 = h f(y+c1, t+h)

# solve given equation: y'= -y/sqrt(x**2+1)+1/(x+sqrt(x**2+1)) with y(0)=0

def f(y,x):
    t=-y/sqrt(x**2+1)+1/(x+sqrt(x**2+1))
    return t

#init. condit.

x_i, y_i = 0.0, 0.0

x_f = 10.0
N=1000
h=(x_f-x_i)/N
px=[]
py=[]
pY=[]

px.append(x_i)
py.append(y_i)
pY.append(y_i)
x_list=arange(x_i, x_f, h)
y=y_i
Y=y_i
for xx in x_list:
    c1=h*f(y, xx)
    c2=h*f(y+0.5*c1, xx+0.5*h)
    c3=h*f(y+0.5*c2, xx+0.5*h)
    c4=h*f(y+c3, xx+h)
    y+=(c1+2*c2+2*c3+c4)/6
    C1=h*f(Y, xx)
    C2=h*f(Y+C1, xx+h)
    Y+=0.5*(C1+C2)
    py.append(y)
    pY.append(Y)
    px.append(xx+h)

print('red dot: 4th order RM  blue star: 2nd order RM')
plot(px,py,'ro')
plot(px,pY,'b*')

show()
