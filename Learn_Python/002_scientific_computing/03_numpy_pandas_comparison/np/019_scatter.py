import numpy as np 
import random
import matplotlib.pyplot as plt

a = []
x = range(1000)
for i in range(1000):
    a.append(random.randint(1,1000))



plt.scatter(x,a) # where -- is the line type and m for magenta color
plt.title("Sin Wave Bar graph") 
plt.xlabel("time") 
plt.ylabel("value") 
plt.show()