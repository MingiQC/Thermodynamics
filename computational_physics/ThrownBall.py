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

def height(v):
    r=array([0.0,v],float)
    for t in arange(t_i, t_f, h):
        r=RK4(r)
    return r[0]

def bisection(v1,v2):
    h1=height(v1)
    h2=height(v2)
    while abs(h2-h1)>tolerance:
        v_m=(v1+v2)/2
        h_m=height(v_m)
        if h1*h_m>0:
            v1=v_m
            h1=h_m
        else:
            v2=v_m
            h2=h_m
    v=(v1+v2)/2
    return v
v1=0.01     #guessed data
v2=1000.0

v=bisection(v1,v2)
print('The required initial velocity is',v,'m/s');

px=[]
pt=[]
px.append(0.0)
pt.append(0.0)
r=array([0.0,v],float)
for t in arange(t_i, t_f, h):
    r=RK4(r)
    px.append(r[0])
    pt.append(t+h)

plt.plot(pt,px)
plt.xlabel(r'$t$')
plt.ylabel(r'$h$')
plt.show()
            
