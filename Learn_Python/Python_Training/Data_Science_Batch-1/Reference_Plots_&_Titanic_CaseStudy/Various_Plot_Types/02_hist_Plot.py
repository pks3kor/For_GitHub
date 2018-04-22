import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
# Generate linearly spaced 50 values
x = np.random.randint(-50,100,200)
y = np.random.randint(-50,100,200)
plt.hist(x,bins=np.arange(-50,100,10),rwidth=.90,align="left",label="x")
plt.hist(y,bins=np.arange(-50,100,10),rwidth=.90,align="left",label="y")
plt.xlabel("bins")
plt.ylabel("no. of occurences")
#~ plt.title("Graph of x**3+y**3 and x**2+y**2")
#~ plt.tet(10,400,"x**3+y**3") # adding text to some x,y position
#~ plt.text(10,-400,"x**2+y**2") # adding text to some x,y position
plt.legend()
plt.show()