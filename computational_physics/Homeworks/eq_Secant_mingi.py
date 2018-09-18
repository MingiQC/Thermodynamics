#2014103332김민기 
from math import exp, log
from numpy import linspace
from pylab import plot, show, xlabel, ylabel

accuracy=1e-12

def f(x):
    y=log(x)*exp(x)-x**2
    return y


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
def Ans(x1,x2):
    delta=1.0
    xl=[x1]
    dl=[]
    while abs(delta)>accuracy:
        delta=(x2-x1)*f(x2)/(f(x2)-f(x1))
        x=x2-delta
        x1,x2=x2,x
        xl.append(x)
        dl.append(delta)
        plot(xl)
        plot(dl)
        ylabel(r'error rate, answer',fontsize=10)
        xlabel(r'iteration rate', fontsize=10)
    return show(), print('Start:',xl[0],'Answer:',xl[-1],'Iteration rate:',len(dl))

Ans(5,9)
Ans(1,4)
Ans(1.5,1.7)

# By nrm method, delta=-f/f'
#find a root of f(x)=0


