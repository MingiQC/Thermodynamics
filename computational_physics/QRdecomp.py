'''
QR decomp.

1. create an N by N matrix V to hold the eigenvectors
2. Initialize V to be equal to the identity matrix I
3. choose a target accuracy e for off-diagonal elements of the eigenvalue matrix(D)
4. calculate the QR decomp. A=QR
5.update A to the new value A=RQ
6. multiply V on the right by Q
7.check the off diagonal elements of A if they are all less tha e we are done. Otherwise go back to step 4

'''
import numpy as np
from numpy.linalg import eigh

A=np.array([[1,4,8,4],[4,2,3,7],[8,3,6,9],[4,7,9,2]],float)
# Right answer
xx, VV = eigh(A)
print('=====Result using linalg.package=====')
print('xx=',xx)
print('VV=',VV)

#Implementation of QR decomp.
epsilon=1e-10
n=A.shape #(4,4)
N=n[1] #4

#V,U,Q,R
V=np.zeros([N,N],float) #1 create N by N  matrix to hold the eigenvectors
U=np.zeros([N,N],float)
Q=np.zeros([N,N],float)
R=np.zeros([N,N],float)
#2. initialize V to be the equal to the identity matrix
for i in range(N):
    V[i,i]=1.0 # Identity matrix
#3. target accuracy : eplison
delta=1.0
while delta>epsilon:
    for i in range(N):  #Gram_schmidt process  calculate Q and R
        U[:,i]=A[:,i]
        if i>0:
            for j in range(i):
                U[:,i]-=(np.dot(Q[:,j],A[:,i])*Q[:,j]) #U_i = A_i - (Q_j dot A_i)Q_j
        magU=np.dot(U[:,i],U[:,i])**(1/2) # Q_i = U_i / abs(U_i)
        Q[:,i]=U[:,i]/magU
    for j in range(N):
        for k in range(N):
            if j>k:
                R[j,k]=0 #upper triangular
            elif j==k:
                R[j,k]=np.dot(U[:,j],U[:,j])**(1/2) #diagonal element=> |u_i|
            else:
                R[j,k]=np.dot(Q[:,j],A[:,k]) #q_j dot a_k
    print('R=',R)
    print('Q=',Q)
    A=np.dot(R,Q) #4. calculate QR = A decomp.
    V=np.dot(V,Q) #6. Mult. V in the right by Q
    delta=0.0 #initilaize delta
    for j in range(N):
        for k in range(N):
            if j<k:
                if delta<abs(A[j,k]):
                    delta=abs(A[j,k]) #off diagonal element 중에서 가장 큰 아이를 잡음
    print(np.dot(R,Q))
    print('delta=',delta)
    input()
x=np.empty(N,float)
for i in range(N):
    x[i]=A[i,i] # diagonal element of diagonal matrix D=> eigenvalue
print('\n===== Result obtained from  QR decomp. code======')
print('x=',x)
print(V) #eigenvector들 의 모 임

#transpose V
VT=np.zeros([N,N],float)
for i in range(N):
    for j in range(N):
        VT[i,j]=V[j,i]
print('VT=',VT)
a=np.array([[1,4,8,4],[4,2,3,7],[8,3,6,9],[4,7,9,2]],float)
print('VT A V=', np.dot(VT,np.dot(a,V))) #the result is diagonal mat.
