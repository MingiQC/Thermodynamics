from numpy.linalg import inv, det
from numpy import array, empty, dot
'''
linear system

2w + 1x + 4y + z = -4
3w + 4x + -1y + -1z = 3
1w + -4x + 1y + 5z = 9
2w + -2x + 1y + 3z = 7

RowReduce[{{2,1,4,1,-4},{3,4,-1,-1,3},{1,-4,1,5,9},{2,-2,1,3,7}}]
'''

A=array([[2,1,4,1,-4],[3,4,-1,-1,3],[1,-4,1,5,9],[2,-2,1,3,7]],float)


print('Ax=v')
print('where A is ')
print(A)
print('divide the first row by the top-left element of the matrix')
A[0,:]=A[0,:]/A[0,0]
print(A)
print('subtract 3 times the first row form the second row')
A[1,:]=A[1,:]-A[1,0]*A[0,:]
print(A)
print('subtract the first row from the third one and also subtract 2 times the first row from the 4th')
A[2,:]=A[2,:]-A[2,0]*A[0,:]
A[3,:]=A[3,:]-A[3,0]*A[0,:]
print(A)
print('divide second row by 2.5')
A[1,:]=A[1,:]/A[1,1]
print(A)
print('subtract -4.5 times the second row from the 3rd ans -3 times the 2nd row from the 4th')
A[2,:]=A[2,:]-A[2,1]*A[1,:]
A[3,:]=A[3,:]-A[3,1]*A[1,:]
print(A)
print('divide the third row by by -13.6:')
A[2,:]=A[2,:]/A[2,2]
print(A)
print('subtract -11.4 times third row from the fourth')
A[3,:]=A[3,:]-A[3,2]*A[2,:]
A[3,:]=A[3,:]/A[3,3]
print(A)
print('the matrix is now upper triangular')
print('to find the final solution of eq. we now use the process of backsubstitution')
z=A[3,4]
y=A[2,4]-A[2,3]*z
x=A[1,4]-A[1,3]*z-A[1,2]*y
w=A[0,4]-A[0,3]*z-A[0,2]*y-A[0,1]*x
print('z=',z,
      'y=',y,
      'x=',x,
      'w=',w)

####################################################################
a=array([[2,1,4,1],[3,4,-1,-1],[1,-4,1,5],[2,-2,1,3]],float)
v=array([-4,3,9,7],float)
N=len(v)
print('the answer is', dot(inv(a),v))
#Gaussian Elimination
for m in range(N):
    #divide by the diagonal element
    div=a[m,m]
    a[m,:]/=div
    v[m]/=div

    #Subtract for the lower rows
    for i in range(m+1, N):
        mult=a[i,m]
        a[i,:]-=mult*a[m,:]
        v[i]-=mult*v[m]
print(a,v)
#Backsubstitution
x=empty(N,float)
for m in range(N-1,-1,-1):
    x[m]=v[m]
    for i in range(m+1,N):
        x[m]-=A[m,i]*x[i]
print(x)
