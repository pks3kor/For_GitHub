import numpy as np 
a = np.arange(1,16).reshape(5,3) 
print a

tmp = np.nonzero(a)
print tmp # returns two array, one with row details and other one with col details

# The where() function returns the indices of elements in an input array where the given condition is satisfied.
tmp = np.where(a>3)
print tmp
print a[tmp]

print 'Extract elements using condition' 
print np.extract(a%2==0, a)