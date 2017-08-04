"""
Author : Pankaj soni
"""

# Stacking multiple arrays in sngle arrays in verticakl and horizontal style
# Note: Dimension of arrays must be same
import numpy as np

a = np.arange(10).reshape(2,5)
print a
b = np.arange(3,13).reshape(2,5)
print b

c = np.vstack((a,b))
print c

d = np.hstack((a,b))
print d

# print cummulative sum of array d
print d.cumsum()

# print whole sum of array d
print d.sum()
