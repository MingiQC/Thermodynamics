#2014103332 김민기 
from math import exp, log
from numpy import linspace
from pylab import plot, show, xlabel, ylabel

accuracy=1e-12

def f(x):
    y=log(x)*exp(x)-x**2
    return y

def df(x):
    dy=log(x)*exp(x)-exp(x)/x-2*x
    return dy

px=linspace(0.01, 3.04, 100)
py=[]
p0=[]
for xx in px:
    py.append(f(xx))
    p0.append(0)
    
plot(px,p0)
plot(px, py)
show()

#Define Ans(x) which return error/answer graph, right answer, iteration rate.
def Ans(x):
    delta=1.0
    xl=[x]
    dl=[]
    while abs(delta)>accuracy:
        delta=f(x)/(df(x))
        x+=delta
        xl.append(x)
        dl.append(delta)
        plot(xl)
        plot(dl)
    return show(), print('Start',xl[0],'Answer:',xl[-1],'iteration rate: ', len(dl))

Ans(0.3)
Ans(1.0)
Ans(1.6946)
Ans(2.1)
Ans(2.4)


# By nrm method, delta=-f/f'
#find a root of f(x)=0
#delta=-f/f'
#f(1)<0, f'(1)>0 -> 1부터 시작하는 게 바람직함.
#Ans(2.4)은 발산함
