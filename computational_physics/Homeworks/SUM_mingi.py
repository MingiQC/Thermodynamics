#2014103332 김민기 

from numpy import linspace
from pylab import show, plot, xlim, ylim

def S_N(x):
    S=0
    for i in range(x):
        S+=1/(i+1)
    return S
print('S_N(2) = ', S_N(2))

def S_N2(x):
    S=0
    for i in range(x):
        S+=1/(i+1)**2
    return S
print('S_N2(2) = ', S_N2(2))

px=linspace(1,100,100)
py1=[]
py2=[]

for xx in px:
    py1.append(S_N(int(xx)))
    py2.append(S_N2(int(xx)))
plot(px, py1)
plot(px, py2)
show()
print(py1[-1])
print(py2[-1])
