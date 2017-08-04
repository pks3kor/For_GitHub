"""
Author : Pankaj soni
"""

# Stacking multiple arrays in sngle arrays in verticakl and horizontal style
# Note: Dimension of arrays must be same
# Plot the obtained sin values from numpy
import numpy as np
import matplotlib.pyplot as plt

a = np.linspace(0,10,100)
#~ print a
print a.std()
print a.var()
print a.mean()
tmp = np.sin(a)
plt.plot(np.sin(a))
plt.show()

