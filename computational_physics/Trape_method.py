from numpy import linspace, array
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

def f(x):
    y=x**4-2*x+1
    return y

def Integrate(x0,xe,n):
    s=0.0
    x=x0
    h=(xe-x0)/n
    for i in range(0,n):
        tmp=f(x+h/2.0)
        # Draw trapezoid
        points=[[x,0],[x+h,0],[x+h,f(x+h)],[x,f(x)]]
        ax1.add_patch(Polygon(points, fill=False, edgecolor='r'))
        s+=tmp
        x+=h
    return(h*s, h)
#To draw a trapezoid
fig=plt.figure()
ax1=fig.add_subplot(111)

N_f=1000
px=[]
py=[]
for xx in linspace(0, 2, N_f):
    py.append(f(xx))
    px.append(xx)
Int_res, dx = Integrate(0, 2, 10)
print('10 slices: ', Int_res)
plt.plot(px, py)
plt.xlim(0,2)
plt.show()

fig=plt.figure()
ax1=fig.add_subplot(111)
Int_res, dx = Integrate(0, 2, 100)
print('100 slices: ', Int_res)
plt.plot(px, py)
plt.xlim(0,2)
plt.show()

fig=plt.figure()
ax1=fig.add_subplot(111)
Int_res, dx = Integrate(0,2,1000)
print('1000 slices: ', Int_res)
plt.plot(px,py)
plt.xlim(0,2)
plt.show()
print('answer: ', 4.4)
