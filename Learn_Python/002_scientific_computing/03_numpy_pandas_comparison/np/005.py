import numpy as np

# Array creation routines
tmp = np.zeros([4,4]) # default is float64
print tmp
print "*"*100

tmp = np.zeros([4,4],dtype=float)
print tmp
print "*"*100

tmp = np.zeros([4,4],dtype=int)
print tmp
print "*"*100

tmp = np.ones([4,4])
print tmp
print "*"*100
