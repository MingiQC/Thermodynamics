# By secant method
'''
<Remark> secant method:
let's find a solution of f(x)=0!
define arbitrary x1,x2 and delta, where delta is
(delta)=(x2-x1)f(x2)/(f(x2)-f(x1))
and then evaluate x1,x2 to x2, x2-delta.
Iterate untill delta is smaller than tolerance.

In BC problem define gg(x,v,xf)=u(xf)-ui
'''
from numpy import array, arange
from matplotlib import pyplot as plt

g=9.81
t_i,t_f=0.0, 10.0
N=1000
h=(t_f-t_i)/N

tolerance=1e-10

def f(r):
    x=r[0]
    v=r[1]
    fx=v
    fy=-g
    return array([fx,fy],float)

def RK4(r):
    k1=h*f(r)
    k2=h*f(r+0.5*k1)
    k3=h*f(r+0.5*k2)
    k4=h*f(r+k3)
    r+=(k1+k2+k3+k4)/6.0
    return r

def gg(x,v,x_f):
    r=array([x,v],float)
    for t in arange(t_i, t_f, h):
        r=RK4(r)
    return (r[0]-x_f)

def secant(r,dv):
    x=r[0]
    v=r[1]
    v1=v+dv
    r1=array([x,v],float)
    while abs(dv)>=tolerance:
        d=gg(x,v1,0.0)-gg(x,v,0.0)
        v2=v1-gg(x,v1,0.0)*(v1-v)/d
        v,v1=v1,v2
        dv=v1-v
    return v

v1=0.01
x_i=0.0
r=array([x_i,v1],float)
v=secant(r,10.0)

print('The required initial velocity is ' ,v,'m/s');

px=[]
pt=[]
px.append(0.0)
pt.append(0.0)
r=array([0.0,v],float)
for t in arange(t_i, t_f,h):
    r=RK4(r)
    px.append(r[0])
    pt.append(t+h)
plt.plot(pt,px)
plt.xlabel(r'$t$')
plt.ylabel(r'$h$')
plt.show()
              
       
