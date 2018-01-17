import numpy as np 
a = np.array([1,2,3])
b = np.array([4,5,6])

print a*b
print np.dot(a,b) #This function returns the dot product of two arrays. 
                #For 2-D vectors, it is the equivalent to matrix multiplication. 
                #For 1-D arrays, it is the inner product of the vectors. 
                #For Ndimensional arrays, it is a sum product over the last axis of a and the second-last axis of b.
print np.add(a,b)
print np.subtract(a,b)
print np.multiply(a,b)
print np.power(a,b)
print np.power(a,b)
print np.mod(a,b)
print np.remainder(a,b) # same as above
