from math import pi, sin
from numpy import linspace
from pylab import plot, show, xlim, ylim, bar

def f(x):
    y=sin(x)
    return y

def Integrate(x0,xe,n):
    s=0.0
    x=x0
    h=(xe-x0)/n
    for i in range(0,n):
        tmp=f(x+h/2.0)
        s+=tmp
        fbar.append(tmp)
        xi.append(x+0.5*(xe-x0)/n)
        x+=h
    return(h*s,h)
fbar=[]
xi=[]

N_f=1000
px=[]
py=[]
for xx in linspace(0.0, pi, N_f):
    py.append(f(xx))
    px.append(xx)
Int_res , dx= Integrate(0, pi, 10)
print('10 slices: ',Int_res)
plot(px,py)
bar(xi, fbar, dx, edgecolor='k',facecolor='None')
ylim(0, 1.1)
xlim(0, pi)
show()

del fbar[:]
del xi[:]
Int_res, dx=Integrate(0,pi,100)
print('100 slices: ', Int_res)
plot(px, py)
bar(xi, fbar, dx, edgecolor='k',facecolor='None')
ylim(0, 1.1)
xlim(0,pi)
show()
