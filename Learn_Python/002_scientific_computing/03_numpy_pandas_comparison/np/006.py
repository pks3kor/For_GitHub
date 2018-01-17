import numpy as np

# Array creation from existing data
a = [1,2,3,4,5]
print a
print type(a)
tmp = np.asarray(a) # from given list
print tmp
print type(tmp)

print np.asarray(range(10)).reshape(2,5) # from range list and reshape

a = "Hello  world" 
print np.frombuffer(a,dtype="S1").reshape(2,6) # for given string or any object which support buffer interface