"""
Author : Pankaj soni
"""

import sys
import numpy as np

gso = sys.getsizeof

a = range(1000)
print str(gso(0))+" Bytes" # For an int value
print str(gso(0.))+" Bytes" # For a float value
print str(gso("a"))+" Bytes" # For a string 
print str(gso("A"))+" Bytes" # For a string
print str(gso([]))+" Bytes" # # For an empty list
print str(gso(a))+" Bytes" # # For an empty list
print str(gso(a)*len(a))+" Bytes" # # For an empty list
print str(gso([[],[]]))+" Bytes" # # For an empty list of list
print str(gso(()))+" Bytes" # # For an empty tuple
print str(gso({}))+" Bytes" # # For an empty dictionary

print "*"*50
a = np.arange(1000,dtype=np.int32)
print a.itemsize*a.nbytes
print a.nbytes
print str(gso(a))+" Bytes" # # For an array of 1000 elements