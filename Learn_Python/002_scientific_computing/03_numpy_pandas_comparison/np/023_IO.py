# File IO usign numpy

import numpy as np 

x = np.arange(-200,200,2)
np.save("np_array1",x) # save to a file with .npy (default extension)
print x 
ld = np.load("np_array1.npy") # load from file along with .npy
print ld