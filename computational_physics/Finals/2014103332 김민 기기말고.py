#2014103332 김민 기 
import numpy as np
import matplotlib.pyplot as plt
hbar=1
m=1
N = 4097
a = 200.0
b = 2.
x = np.linspace(-a/2.,a/2.,N)
h = x[1]-x[0] # 간 격
V=np.zeros(N)  #potential
V0=20
for i in range(N):
    if x[i]< -b/2. or x[i]> b/2.:
        V[i]= V0

Mdd = 1./(h*h)*(np.diag(np.ones(N-1),-1) -2* np.diag(np.ones(N),0) + np.diag(np.ones(N-1),1))
# Banded matrix : laplacian( by jacobi method) therefore the hamiltonian is,
H = -(hbar*hbar)/(2.0*m)*Mdd + np.diag(V)  #eigenvalue eq. with banded mat.
E,psiT = np.linalg.eigh(H) #for energy eigenvalue and eigenvector
psi = np.transpose(psiT)
# take the transpose of psiT to the wavefunction vectors can accessed as psi[n]
plt.figure(figsize=(10,7))
plt.xlim((-3*b,3*b))
plt.plot(x,V,color="Gray",label="V(x) ")
for i in range(2):
    if E[i]<V0:                 # only bound states!
        if psi[i][N-10] < 0:   # Flip the wavefunctions if it is negative at large x, so plots are more consistent.
            plt.plot(x,-psi[i]/np.sqrt(h),label="$E_{}$={:>8.3f}".format(i,E[i]))
        else:
            plt.plot(x,psi[i]/np.sqrt(h),label="$E_{}$={:>8.3f}".format(i,E[i]))
plt.legend()
plt.show()
