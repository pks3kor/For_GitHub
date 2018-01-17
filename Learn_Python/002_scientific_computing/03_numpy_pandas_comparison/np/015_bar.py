import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(0,10*np.pi,0.1)
y = np.sin(x)


plt.bar(x,np.sin(x), color = 'g', align = 'center') # where -- is the line type and m for magenta color
plt.title("Sin Wave Bar graph") 
plt.xlabel("time") 
plt.ylabel("value") 
plt.show()