from numpy import array, zeros, empty, copy, dot
from numpy.linalg import inv
A=array([[0,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)
n=A.shape  #(4 by 4)
N=n[1]  #4
L=zeros([N,N],float)
U=empty([N,N],float)
U=copy(A)
V=zeros([N,N],float)
for m in range(N):
    V[m,m]=1.0
print('A=',A)
print('U=',U)
print('V=',V)
print('For comparison, inv(A)=',inv(A))

#G_E with LUD
for m in range(N):
    #applying partial pivoting
    pivot_max=abs(U[m,m])
    pivot_point=m
    for i in range(m+1,N):
        pivot_tmp=abs(U[i,m])
        if pivot_tmp > pivot_max:
            pivot_point, pivot_max = i, pivot_tmp
    if m!=pivot_point:
        for i in range(N):
            U[m,i], U[pivot_point,i]=U[pivot_point,i],U[m,i]
            L[m,i], L[pivot_point,i]=L[pivot_point,i],L[m,i]
            A[m,i], A[pivot_point,i]=A[pivot_point,i],A[m,i]
            V[m,i], V[pivot_point,i]=V[pivot_point,i],V[m,i]

    L[m:,m]=U[m:,m]
     #divide by the diagonal element
    div=U[m,m]
    U[m,:]/=div

    #Subtract from the lower rows
    for i in range(m+1,N):
        mult=U[i,m]
        U[i,:]-=mult*U[m,:]
print('\n')
print('Now we have L and U')
print('L')
print(L)
print('U')
print(U)
Y=empty([N,N],float)
for j in range(N):  #for each col
    for m in range(N):   #for each row
        Y[m,j]=V[m,j]
        for i in range(m):
            Y[m,j]-=L[m,i]*Y[i,j]
        Y[m,j]/=L[m,m]
X=empty([N,N],float)
for j in range(N):
    for m in range(N-1,-1,-1):
        X[m,j]=Y[m,j]
        for i in range(m+1,N):
            X[m,j]-=U[m,i]*X[i,j]
        X[m,j]/=U[m,m]
print('\n')
print('X=',X)
