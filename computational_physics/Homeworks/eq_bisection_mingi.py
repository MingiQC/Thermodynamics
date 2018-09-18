#2014103332 김민기 
from math import exp, log
from numpy import linspace
from pylab import plot, show, ylim, xlabel, ylabel

def f(x):
    y = exp(x)*log(x)-x**2
    return y

#Constants

Tmax = 4.0
points = 10000
accuracy = 1e-6

#set up lists for plotting
y = []
temp = linspace(0.9, Tmax, points)

#Loop for temperature
for T in temp:
    a = 1.0
    b = 4.0
    error = 3.0

    #Loop for solving Equation
    while error>accuracy:
        x0 = (a+b)/2.0
        if f(a)*f(x0)<0:
            b = x0
        else:
            a = x0
        error = abs(a-b)

    y.append((a+b)/2.0)

#Plot the graph
plot(temp,y)
ylim(-3.1, 3.1)
show()
print(y[0], y[-1])
