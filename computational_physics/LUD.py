'''
LU decomposition

Not only L is lower triangular, but its elements are easily obtained through Gauss-Jordan elimination.
'''
from numpy import array, zeros, empty, copy, dot
from numpy.linalg import solve

A=array([[0,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)
v=array([-4,3,9,7],float)
N=len(v)
L=zeros([N,N],float)
U=empty([N,N],float)
U=copy(A)

print('A=',A)
print('U=',U)

#Gaussian elimination with LU decomposition
for m in range(N):  #4
    #partial pivoting  (choose largest under-diagonal element (abs))
    pivot_max=abs(U[m,m])
    pivot_point=m
    for i in range(m+1,N):
        pivot_tmp=abs(U[i,m])
        if pivot_tmp>pivot_max:
            pivot_point, pivot_max=i, pivot_tmp
    if m!=pivot_point:
        for i in range(N):
            U[m,i],U[pivot_point, i]=U[pivot_point, i],U[m,i] #pivot point  행 과 m행 을 자 리바꾸 기
            L[m,i],L[pivot_point, i]=L[pivot_point, i],L[m,i]
            A[m,i],A[pivot_point, i]=A[pivot_point, i],A[m,i]
        v[m],v[pivot_point]=v[pivot_point],v[m]

    L[m:,m]=U[m:,m]
    print('A=',A)
    print('L=',L)
    print('U=',U)
    input()
    #Divide by the diagonal element
    div=U[m,m]
    U[m,:]/=div

    #subtract from the lower rows
    for i in range(m+1,N):
        mult=U[i,m]
        U[i,:]-=mult*U[m,:]

print()
print('After GE with LU decomposition')
print()
print('L=',L)
print()
print('A=',A)
print()
print('LU=',dot(L,U))

#backsubtraction
y=empty(N,float)
for m in range(N):
    y[m]=v[m]
    for i in range(m):
        y[m]-=L[m,i]*y[i]
    y[m]/=L[m,m]

x=empty(N,float)
for m in range(N-1,-1,-1):
    x[m]=y[m]
    for i in range(m+1,N):
        x[m]-=U[m,i]*x[i]
    x[m]/=U[m,m]
print('\n')
print('x=',x)
print('solve(A,v)=',solve(A,v))
