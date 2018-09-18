#Thrown ball problem with relaxation method ------ Relax 부 분다시보기!------
from numpy import array, arange, ones, copy, max
from pylab import plot, show, xlabel, ylabel, legend

g=9.81
t_i, t_f = 0.0 , 10.0
N=100
h=(t_f-t_i)/N

def f():
    return (-g)
t=list(arange(t_i,t_f,h)) # t 를쪼개 기0~10까 지h 간격으 로
t.append(t[len(t)-1]+h) # t[len(t)-1]=> len(t)-1=101-1=100, t[100]+h 를 append 해 라
t[0]=0.0
leng_t=len(t)
x=list(ones(leng_t,float)) # 1 만101 개있 는리스트 를만들 기
i=1
for i in range(1,leng_t-1):   #(1~100)까 지  i 
    x[i]=20.0
x[0]=0.0 #boundary condition x(t_i)=0
x[leng_t-1]=0.0 #boundary condition x(t_f)=0
xtmp=copy(x)
w=0.8
tolerance=1e-6
delta=1.0
while delta>tolerance:
    for i in range(leng_t):
        if i==0 or i==leng_t-1:
            xtmp[i]=x[i]
        else:
            xtmp[i]=(x[i+1]+x[i-1]-f()*h**2)/2.0
    delta=max(abs(x-xtmp))
    x, xtmp = xtmp, x
plot(t,x)
xlabel(r'$t$')
ylabel(r'$h$')
show()
