import numpy as np
import matplotlib.pyplot as plt
#~ plt.style.use('seaborn-whitegrid')
# Generate linearly spaced 50 values
x = np.linspace(-2,20,50)
y = np.linspace(-.9,-20,50)
z1 = x**3+y**3
z2 = x**2+y**2
#~ z = np.sin(x)
plt.plot(x,z1,"--b",label="x**3+y**3")
plt.plot(x,z2,".r",label="x**2+y**2")
plt.xlabel("x-val")
plt.ylabel("y-val")
#~ plt.title("Graph of x**3+y**3 and x**2+y**2")
plt.legend()
plt.text(10,400,"x**3+y**3") # adding text to some x,y position
plt.text(10,-400,"x**2+y**2") # adding text to some x,y position
plt.show()