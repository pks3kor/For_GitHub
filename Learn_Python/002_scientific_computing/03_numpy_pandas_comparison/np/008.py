import numpy as np 

# Resizing an array

a = np.arange(1,10).reshape(3,3)
print a # Original array
print np.resize(a,[2,2]) # make 2,2 of original array
print np.resize(a,[3,2]) # make 3,2 of original array
print np.resize(a,[3,4]) # make 3,4 of original array, since new size or bigger than original hence start copying value from original array and fill to new array
print np.resize(a,[4,3]) # make 4,3 of original array, since new size or bigger than original hence start copying value from original array and fill to new array

# Append to an array'
a = np.arange(1,10).reshape(3,3)

print np.append(a,[[9,10,11]]) # If no axis is given then all the value wil be flatten
print np.append(a,[[9,10,11]],axis=0) # If axis=0 is given then the new element will be appended along with row axis
print np.append(a,[[9,10,11],[12,13,14],[15,16,17]],axis=1) # If axis=1 is given then the new element (dimension must be same as original array )
                                                            #will be appended along with col axis and 