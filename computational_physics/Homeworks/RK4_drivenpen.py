#2014103332 김민기
from math import sin, cos,pi
from pylab import plot, xlabel, ylabel, show, legend
#(d2/dt2)(theta)=-g(d/dt)(theta)-sin(theta)+bcos(w_0 t)
#=f(theta,v,t)=-qv-sin(theta)+bcos(w_0 t)
#k1=hf(theta,v,t)
#k2=hf(x+hv/2,v+k1/2,t+h/2)
#k3=hf(x+hv/2+hk1/4,v+k2/2,t+h/2)
#k4=hf(x+hv+hk2/2,v+k3,t+h)
#x+=hv+h(k1+k2+k3)/6
#v+=(k1+2k2+2k3+k4)/6

def f(theta,v,t):
    w_0=2/3
    q=0.5
    b=1.2
    y=-q*v-sin(theta)+b*cos(w_0*t)
    return y

#init. condit.
t_i=0.0
theta_i=0.25*pi  # 약 45도
v_i=0

t_f=100.0 # end of the interval
h=0.001
pt=[]
ptheta=[]
pv=[]

theta=theta_i
v=v_i
t=t_i

ptheta.append(theta)
pv.append(v)
pt.append(t)

while t<=t_f:
    k1=h*f(theta,v,t)
    k2=h*f(theta+0.5*h*v,v+0.5*k1,t+0.5*h)
    k3=h*f(theta+0.5*h*v+0.25*h*k1,v+0.5*k2,t+0.5*h)
    k4=h*f(theta+h*v+0.5*h*k2,v+k3,t+h)
    theta+=h*v+h*(k1+k2+k3)/6.0
    v+=(k1+2*k2+2*k3+k4)/6.0
    t+=h
    ptheta.append(theta)
    pv.append(v)
    pt.append(t)

plot(pt,ptheta, 'r', label=r'$\theta$')
plot(pt,pv,'g',label='v')
xlabel(r'$t$')
ylabel(r'$\theta$ $v$')
legend(loc='upper right')
show()

plot(ptheta, pv,'r')
xlabel(r'$\theta$')
ylabel(r'$v$')
show()

# b=약 0.44~0.48일때 거의 simple harmonic oscillator
# 0.44보다 작아질때 damping, 0.5보다 커질때 diverge
