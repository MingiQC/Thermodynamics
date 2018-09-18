#2014103332 김민기
from math import exp
from numpy import linspace, array
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

def f(x):
    y=exp(x)
    return y

def Integrate(x0,xe,n):
    s=0.0
    x=x0
    h=(xe-x0)/n
    for i in range(0,n):
        tmp=f(x+h/2.0)
        # Draw trapezoid
        points=[[x,0],[x+h,0],[x+h,f(x+h)],[x,f(x)]]
        ax1.add_patch(Polygon(points, fill=False, edgecolor='g'))
        s+=tmp
        x+=h
    return(h*s, h)
#To draw a trapezoid
fig=plt.figure()
ax1=fig.add_subplot(111)

N_f=1000
px=[]
py=[]
for xx in linspace(0, 2.5, N_f):
    py.append(f(xx))
    px.append(xx)
Int_res, dx = Integrate(0, 2.5, 1000)
print('1000 slices: ', Int_res)
plt.plot(px, py)
plt.xlim(0,2.5)
plt.show()
print('answer :', exp(2.5)-1)
