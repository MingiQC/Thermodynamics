from math import sin, pi
from numpy import arange, array
from pylab import plot, xlabel, ylabel, show

g=9.81
l=0.1

def f(r,t):
    theta=r[0]
    omega=r[1]
    f_theta=omega # omega = (d/dt) theta
    f_omega=-(g/l)*sin(theta)  # (d/dt) omega = -(g/l)sin(theta)
    return array([f_theta,f_omega],float)

# init. condit.
t_i=0.0
theta_i=pi-0.1
omega_i=0.0

t_f=5.0 # end of the interval to calculate
h=0.00001
pt=[]
ptheta=[]
pomega=[]
r=[theta_i,omega_i]

theta=theta_i #pi-0.5
omega=omega_i #0
t=t_i #0

pt.append(t)
ptheta.append(theta)
pomega.append(omega)

while t<=t_f:
    r+=h*f(r,t) # \delta f_theta, \delta f_omega
    t+=h
    ptheta.append(r[0])
    pomega.append(r[1])
    pt.append(t)

plot(pt,ptheta,'r')
plot(pt,pomega,'b')
xlabel(r"$t$", fontsize=20)
ylabel(r'$\theta$, $\omega$', fontsize=20)
show()

plot(ptheta, pomega)
xlabel(r'$\theta$', fontsize=20)
ylabel(r'$\omega$', fontsize=20)
show()
