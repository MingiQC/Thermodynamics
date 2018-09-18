#2014103332 김민 기
import numpy as np
from numpy import empty,zeros,max,copy
from pylab import imshow,gray,show
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

'''
By using relaxation method, compute the potential distribution between the two concentric square
cylinders shown in the fig.
'''
#constant
M=100  #Grid squrares on a side
Vout=10
Vin=5
tolerance=1e-6

#Create arrays to hold the potential

phi=zeros([M+1,M+1],float) #empty 101 by 101 matrix
phitmp=empty([M+1,M+1],float)
for i in range(40,60):
    phi[i,40],phi[i,60]=Vin, Vin
for j in range(40,60):
    phi[40,j],phi[60,j]=Vin, Vin
phi[0,:],phi[M,:]=Vout, Vout
phi[:,0],phi[:,M]=Vout, Vout  #Boundary condit.

#Main loop
delta=1.0
while delta>tolerance:
    for i in range(M+1):
        for j in range(M+1):
            if i==0 or i==M or j==0 or j==M or i==40 or i==60 or j==40 or j==60:
                phitmp[i,j]=phi[i,j]
            else:  #calculate maximum difference from the old values
                phitmp[i,j]=(phi[i-1,j]+phi[i+1,j]+phi[i,j-1]+phi[i,j+1])/4  #Relaxation method!!
    delta=max(abs(phi-phitmp))

    phi,phitmp=phitmp,phi

imshow(phi)
gray()
show()

#3d plot
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
px=[]
py=[]
pz=[]
for ii in range(M+1):
    for jj in range(M+1):
        px.append(ii)
        py.append(jj)
        pz.append(phitmp[ii,jj])
        
ax.scatter(px,py,pz)

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')


plt.show()
