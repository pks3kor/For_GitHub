import numpy as np

# Create an vector
tmp = np.array([1,2,3,4,5])
print tmp
print "*"*100
print type(tmp)
print "*"*100
print tmp.size
print "*"*100
print tmp.shape
print "*"*100

tmp2 = np.array([[1,2,3],[4,5,6]])
print tmp2
print "*"*100
print type(tmp2)
print "*"*100
print tmp2.size
print "*"*100
print tmp2.shape # tuple or row,col

tmp3 = np.arange(12).reshape(3,4) # 3-row, 4-col, 3*4 ==12
tmp4 = np.arange(12).reshape(2,2,3) # same size 2-times with 2-row, 3-col, 2*2*3 ==12
tmp5 = np.arange(12).reshape(6,2,1) # same size 6-times with 2-row, 1-col, 6*2*1 ==12
print tmp3
print "*"*100
print tmp4
print "*"*100
print tmp5
print "*"*100
tmp6 = np.linspace(1,2) # Crate an arrary equally distributed between given numbers start and end. By default 50 numbers equally divided
print tmp6
print tmp6.size
print "*"*100
tmp7 = np.linspace(1,10,30) # Crate an arrary equally distributed between given numbers start and end. with 30 numbers equally divided
print tmp7
print tmp7.size
print tmp7.dtype
print "*"*100