import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
# Generate linearly spaced 50 values
#~ x = np.random.randint(-50,100,200)
y1 = np.random.randint(-50,100,50)
y2 = np.random.randint(-50,100,50)
plt.bar(np.linspace(1,len(y1),len(y1)),y1,label="y1")
plt.bar(np.linspace(1,len(y1),len(y1))+.3,y2,label="y2")
plt.legend()
plt.show()