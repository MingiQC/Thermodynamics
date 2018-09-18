from numpy import zeros, empty
from pylab import plot, show
from numpy.linalg import solve
'''
N개 의 물질 로이루어 진 계
mZ_i''=k(Z_{i+1}-Z_{i})+k(Z_{i-1}-Z_{i})+F_i

-mw^2x1 = k(x2-x1)+C
-mw^2xi = k(x_{i+1}-x_i)+k(x_{i-1}-x_i)
-mw^2x_N = k(x_{N-1}-x_N)
(a-k) -k                                         C
  -k     a     -k                                |0
         -k      a     -k                        | 0
                   .....                           |0
                                  -k  (a-k)     |0
'''
#Cosntants
N=26
C=1.0
m=1.0
k=6.0
omega=2.0
alpha=2*k-m*omega**2

#Set up the initial values of the array
A=zeros([N,N],float)

for i in range(N-1):
    A[i,i]=alpha
    A[i,i+1]=-k
    A[i+1,i]=-k

A[0,0]-=k
A[N-1,N-1]=alpha-k  # 위 에나 온 행 렬만들 기

v=zeros(N,float)
v[0]=C
#To compare the results with linalg package
xx=solve(A,v)

#perfoem the GE
for i in range(N-1):
    div=A[i,i]
    A[i,i+1]/=div
    v[i]/=div

#now subtract it from the next row down
    if i==N-2:
        n=2
    else:
        n=3
    a_tmp=A[i+1,i]
    for j in range(n):
        A[i+1,i+j]-=A[i,i+j]*a_tmp
    v[i+1]-=a_tmp*v[i]

#Divide the last element of v by the last diagonal element
v[N-1]/=A[N-1,N-1]
#backsubstitution
x=empty(N,float)
x[N-1]=v[N-1]
for i in range(N-2,-1,-1):
    x[i]=v[i]-A[i,i+1]*x[i+1]

#plot the result
plot(x)
plot(x,'ko', ms=15.0)
plot(xx,'rs')
show()
