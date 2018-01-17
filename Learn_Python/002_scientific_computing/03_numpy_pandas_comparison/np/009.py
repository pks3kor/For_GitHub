import numpy as np 
a = np.arange(1,16).reshape(5,3) 

# min and max of array along any axis
print 'Our array is:' 
print a
print '\n'  

print 'Applying amin() function:' 
print np.amin(a,1) 

print 'Applying amax() function:' 
print np.amax(a,1) 

print 'Applying amin() function:' 
print np.amin(a,0) 

print 'Applying amax() function:' 
print np.amax(a,0) 

