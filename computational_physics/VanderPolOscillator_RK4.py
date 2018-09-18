from math import sin, pi
from numpy import arange, array
from pylab import plot, xlabel, ylabel, show, legend
#Van der Pol oscillator: x''=u(x0^2-x^2)x'-w^2 x or x''=f(t,x,v)=u(x_0^2-x^2)v-w^2 x
#x_0=1, u=1, w=1 are given

def f(x,v,t):
    omega=1.0
    mu=1.0
    x_0=1.0
    y=mu*(x_0**2-x**2)*v-omega**2*x
    return y

#init. condit.
t_i=0.0
x_i=5.0
v_i=-2.0

t_f=100.0 # end of the interveal to calculate
h=0.001 # number of steps
pt=[]
px=[]
pv=[]

x=x_i
v=v_i
t=t_i

pt.append(t)
px.append(x)
pv.append(v)

while t<=t_f:
    k1=h*f(x,v,t)
    k2=h*f(x+0.5*h*v,v+0.5*k1, t+0.5*h)
    k3=h*f(x+0.5*h*v+0.25*h*k1,v+0.5*k2, t+0.5*h)
    k4=h*f(x+h*v+0.5*h*k2,v+k3,t+h)
    x+=h*v+h*(k1+k2+k3)/6.0
    v+=(k1+2*k2+2*k3+k4)/6.0
    t+=h
    px.append(x)
    pv.append(v)
    pt.append(t)

plot(pt,px,'r',label='x')
plot(pt,pv,'b',label='v')
xlabel(r'$t$')
ylabel(r'$x$, $y$')
legend(loc='upper right')
show()

plot(px,pv)
xlabel(r'$x$')
ylabel(r'$v$')
show()
