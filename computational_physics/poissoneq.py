from numpy import empty, zeros, max, copy
from pylab import imshow, gray, show

#Constants
M=100
V=1.0
h=0.01
tolerance=1e-6

#Create arrays to hold potential

phi=zeros([M+1,M+1],float)
phitmp=empty([M+1,M+1],float)
rho=zeros([M+1,M+1],float)

#initialize rho
for i in range(60,80):
    for j in range(20,40):
        rho[i,j]=1.0
        rho[j,i]=-1.0
#main loop
delta=1.0
while delta>tolerance:
    #Calculate new values of the potential
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or i==M or j==0 or j==M:  #b.c V=0
                phitmp[i,j]=phi[i,j]
            else:
                phitmp[i,j]=(phi[i-1,j]+phi[i+1,j]+phi[i,j-1]+phi[i,j+1]-rho[i,j]*h**2)/4
    delta=max(abs(phi-phitmp))

    phi=copy(phitmp)

imshow(phi)
gray()
show()
