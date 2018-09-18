import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
N,p=5,1e-1
s1=np.random.binomial(N,p,10000)

n, bins, patches = plt.hist(x=s1, bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('My Very Own Histogram')
plt.text(23, 45, r'$\mu=15, b=3$')
plt.axis([0,6,0,10000])
plt.show()

'''
n,p=5,1e-1
s1=np.random.binomial(n,p,10000)
'''
