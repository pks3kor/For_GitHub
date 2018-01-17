"""
Author : Pankaj soni
"""

import numpy as np

tmp = np.arange(6)
print tmp
# tmp = np.arange(6)
#~ print tmp.shape
#~ print tmp.ndim
#~ print tmp.dtype
#~ print tmp.itemsize
#~ print tmp.size
#~ print type(tmp)

tmp = np.arange(6).reshape(3,2)
# tmp = np.arange(6)
#~ print tmp.shape
#~ print tmp.ndim
#~ print tmp.dtype
#~ print tmp.itemsize
#~ print tmp.size
#~ print type(tmp)

# Convert list/tuple/dict to numpy array
a = range(100)
#~ a = (1,2,3)
#~ print a
#~ a = {"A":2,"B":3}
#~ print a
b = np.asarray(a)
print b

# Convert string to numpy array
a = "Test1"
b = np.frombuffer(a,dtype = 'S1')
print b

# NaN (not a number) check
a = np.array([1,2,np.nan,3,np.nan])
print a[~np.isnan(a)]
print a

# Reshape
a = np.array([1,2,3,4,5,6])
a = a.reshape(2,3)
#~ print a.shape
a = a.reshape(6,1)
#~ print a

# np Iteration
a = np.array([1,2,3,4,5,6])
a = a.reshape(3,2)
for i in np.nditer(a):
    print i,