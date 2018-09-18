from numpy import empty,zeros,max,copy
from pylab import imshow, gray, show
'''
given equation: \laplacian^2\phi(x,y)=0
with B.C V=1volt, grid spacing h=1cm, L=1m ->construct 101 by 101 matrix
'''
#constants
M=100  #Grid squares on a side
V=1.0
tolerance=1e-6

#Create arrays to hold potential

phi=zeros([M+1,M+1],float)  # construct empty 101 by 101 matrix each grid will be the value of potential
phi[0,:]=V  #boundary condit. matrix 의제 일 윗부 분 그래프상으 로하얀부분 이 될것...
phitmp=empty([M+1,M+1],float) #101 by 101 identity matrix

#Main loop
delta=1.0
while delta>tolerance:
    for i in range(M+1):        #Calculate new values of the potential
        for j in range(M+1):
            if i==0 or i==M or j==0 or j==M:  #Boundary condition!
                phitmp[i,j]=phi[i,j]
            else:           #Calculate maximum difference from the old values
                phitmp[i,j]=(phi[i-1,j]+phi[i+1,j]+phi[i,j-1]+phi[i,j+1])/4  #Relaxation method in 2-dim
    delta=max(abs(phi-phitmp))

    phi,phitmp=phitmp,phi

imshow(phi)
gray()
show()
