from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
M=10
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# load some test data for demonstration and plot a wireframe
X=np.arange(0,M,1)
Y=np.arange(0,M,1)
X,Y=np.meshgrid(X,Y)
Z=X+Y
ax.plot_wireframe(X, Y, Z, rstride=5, cstride=5)

plt.show()
