import numpy as np

# Create an vector and reshape
tmp = np.array([1,2,3,4,5,6]).reshape(2,3)
print tmp
print "*"*100

# Create an array and reshape
tmp = np.array([[1,2,3],[4,5,6]]).reshape(6,1) # 6-row and 1-col
print tmp
print "*"*100

# Create an array and reshape
tmp = np.array([[1,2,3],[4,5,6]])
print tmp
print "*"*100
tmp = np.array([[1,2,3],[4,5,6]]).reshape(1,6) # 1-row and 6-col
print tmp
print "*"*100

# array stacking
a = np.array([1,2,3])
b = np.array([4,5,6])
print b.flatten() # Collapse the array in one dimension
print "*"*100
print np.hstack([a,b]) # Stacking arrays horizonatally in one dimension
print "*"*100
print np.vstack([a,b]) # Stacking arrays horizonatally in one dimension
print "*"*100
print np.stack([a,b],0) # Stacking arrays along with axis-0(row)
print "*"*100
print np.stack([a,b],1) # Stacking arrays with axis-1(col)
print "*"*100
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[7,8,9],[10,11,12]])
print np.stack([a,b],0) # Stacking arrays along with axis-0(row)
print "*"*100
print np.stack([a,b],1) # Stacking arrays with axis-1(col)
print "*"*100