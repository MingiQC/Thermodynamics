from numpy import array, empty

A=array([[0,1,4,1],
    [3,4,-1,-1],
    [1,-4,1,5],
    [2,-2,1,3]],float)

v=array([-4,3,9,7],float)
N=len(v)
print(A)
# Gaussian Elimination
for m in range(N):
    # Applying partial pivoting
    pivot_max=abs(A[m,m])
    pivot_point=m
    for i in range(m+1,N):
        pivot_tmp=abs(A[i,m])
        if pivot_tmp>pivot_max:
            pivot_point,pivot_max=i,pivot_tmp
    if m!=pivot_point:
        for i in range(N):
            A[m,i],A[pivot_point,i]=A[pivot_point,i],A[m,i] #열 바꾸기 
        v[m],v[pivot_point]=v[pivot_point],v[m]

    print(A)
    input()
    # Divide by the diagonal element
    div=A[m,m]
    A[m,:]/=div
    v[m]/=div

    #Subtract for the lower rows
    for i in range(m+1,N):
        mult=A[i,m]
        A[i,:]-=mult*A[m,:]
        v[i]-=mult*v[m]
x=empty(N,float)
for m in range(N-1,-1,-1):
    x[m]=v[m]
    for i in range(m+1,N):
        x[m]-=A[m,i]*x[i]
print(x)

    

