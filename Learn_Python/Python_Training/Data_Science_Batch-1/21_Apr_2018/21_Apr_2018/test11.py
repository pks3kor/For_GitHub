import numpy as np

a = np.arange(1,11)
b = np.arange(11,21)
a = a.reshape(2,5)
b = b.reshape(2,5)
#~ print a
#~ print b
print np.vstack((a,b)).shape
print np.hstack((a,b)).shape