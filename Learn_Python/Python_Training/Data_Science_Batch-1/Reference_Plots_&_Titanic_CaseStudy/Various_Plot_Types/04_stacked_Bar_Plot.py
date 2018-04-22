import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
# Generate linearly spaced 50 values
#~ x = np.random.randint(-50,100,200)
#~ y1 = np.random.randint(-50,100,50)
#~ y2 = np.random.randint(-50,100,50)
y1 = [1,2,3,4,5,6]
y2 = [3,2,5,2,6,1]
plt.bar(np.linspace(1,len(y1),len(y1)),y1,label="y1")
for i in range(len(y1)):
    plt.text(np.linspace(1,len(y1),len(y1))[i],y1[i]-.6,y1[i]) # adding text to some x,y position
plt.bar(np.linspace(1,len(y1),len(y1)),y2,label="y2",bottom=y1)
for i in range(len(y1)):
    plt.text(np.linspace(1,len(y1),len(y1))[i],y1[i]+y2[i]+.1,y2[i]) # adding text to some x,y position
plt.legend()
plt.show()