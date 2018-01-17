import numpy as np 
import random
import matplotlib.pyplot as plt
a = []
b = []
c = []
for i in range(1000):
    a.append(random.randint(1,1000))
    b.append(random.randint(1,1000))
    c.append(random.randint(1,1000))
#~ a = range(10000)
#~ print a
min = min(a)
max = max(a)
bin = range(min,max,23)
print bin
#~ plt.hist(a, bin,color="y") 
#~ plt.hist(b, bin,color="g") 
plt.hist(c, bin,color="b") 
#~ plt.plot(bin,bin,"r--")
plt.title("histogram") 
plt.grid(True)
plt.show()