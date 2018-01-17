import numpy as np

# Iteratign over array
tmp = np.arange(20).reshape(5,4)
print tmp
print "*"*100

print tmp.T
print "*"*100

for i,v in enumerate(tmp):   # usign enumerate method
    print i,v

for x in np.nditer(tmp):   # using np.nditer method
    print x,