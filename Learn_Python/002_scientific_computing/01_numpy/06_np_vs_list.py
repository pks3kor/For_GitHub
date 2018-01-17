"""
Author : Pankaj soni

Calculate time taken by list and np.array execution

- Less size
- less computation time
- Convenient ti define and operate

"""

import numpy as np
import sys
import time

size = 10000000
l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 =  np.arange(size)

# Get the size of list and np.array

print sys.getsizeof(1)*len(a1)
print a1.size*a1.itemsize

# for list
start = time.time()
result = [x+y for x,y in zip(l1,l2)]
#~ print result
print str((time.time()-start)*1000)+" ms"

# For np array
start = time.time()
result = a1+a2
#~ print result
print str((time.time()-start)*1000)+" ms"
