import numpy as np 
a = np.arange(1,16).reshape(5,3) 
#~ print a
#~ print id(a)

print id(a)
b =a 
print a is b # 
print id(b)
b.shape = 3,5#np.append(b,[[1,2,3]],axis=0) # If no axis is given then all the value wil be flatten
print b
print a # U see here, a also got modified

tmp = a.view() # create a view only or shallow copy of original array
print tmp
print a is tmp #qqqq 
print np.append(tmp,[[1,2,3,4,5]],axis=0) # If no axis is given then all the value wil be flatten
print a # U see here, a is not modified

b = a.copy() # create a deep copy, 
print b
print np.append(b,[[1,2,3,4,5]],axis=0) # If no axis is given then all the value wil be flatten
print a # U see here, a is not modified