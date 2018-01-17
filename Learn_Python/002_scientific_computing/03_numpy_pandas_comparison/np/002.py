import numpy as np

# artithmetic operation for 2 arrays
a = np.array([1,2,3])
b = np.array([4,5,6])
print a+b
print a*b
print a/b
print a+b
print a**b # Square
print a&b # Logical AND
print a|b # Logical OR
print a^b # Logical XOR
print a==b # Logical comparison
print a>=b # Logical comparison
print a<=b # Logical comparison
print a!=b # Logical comparison

print np.concatenate([a,b]) # Conatenating two arrays
print np.concatenate((a,b)) # Conatenating two arrays
print np.concatenate((a,b),axis=0) # Conatenating two arrays

a = np.array(([1,2,3],[4,5,6]))
b = np.array(([7,8,9],[10,11,12]))
print np.concatenate((a,b),axis=0) # Conatenating two arrays along axis 0
print np.concatenate((a,b),axis=1) # Conatenating two arrays along axis 1
