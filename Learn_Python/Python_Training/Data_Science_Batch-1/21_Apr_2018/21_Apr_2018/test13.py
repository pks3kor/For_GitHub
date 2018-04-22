import numpy as np

a = np.arange(20)
a = a.reshape(5,4)
tmp = a[:,1]
print tmp[tmp>9]
print a
idx = np.where(a<10)
print a[idx]