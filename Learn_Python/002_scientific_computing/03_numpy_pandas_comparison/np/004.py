import numpy as np

# Create an vector and reshape
tmp = np.arange(20).reshape(5,4)
print tmp
print "*"*100

# Slicing
print tmp.shape
print tmp[...]  # All row all col
print tmp[:,:] # All row all col
print "*"*100
print tmp[:,1:] # All row all 1-col onwards
print "*"*100
print tmp[1:,:] # 1-row onwards and all col
print "*"*100
print tmp[::-1,:] # all-row from bottom and all col
print "*"*100
print tmp[::,::-1] # all-row and all col from right most
print "*"*100
print tmp[::-1,::-1] # all-row from bottom and all col from right most
print "*"*100
print tmp[1,2] # 1st-row 2nd-col
print "*"*100

# Advance indexing
print tmp[tmp>4] # Return all value from given array which is greater the 4
print "*"*100




