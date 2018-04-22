import numpy as np
import matplotlib.pyplot as plt
#~ plt.style.use('seaborn-whitegrid')
# Generate linearly spaced 50 values
x = np.zeros((100))
y = np.ones((100))
print y
y1 = np.random.randint(1,100,100)
y2 = np.random.randint(1,100,100)
#~ y1 = [1,2,3,4,5,6]   
#~ y2 = [3,2,5,2,6,1]
#~ plt.scatter(np.linspace(0,len(y1),len(y1)),y1,s=200*np.pi*np.random.rand(1000)**2,c=np.random.rand(len(y1)),alpha=0.5) # alpha is for setting transparent levels
#~ plt.plot(np.linspace(0,len(y1),len(y1)),y1)
plt.scatter(x,y1)
plt.scatter(y,y2)
#~ for i in range(len(y1)):
    #~ plt.text(np.linspace(0,len(y1),len(y1))[i],y1[i]+.3,y1[i])
    #~ plt.text(np.linspace(1,len(y1),len(y1))[i],y1[i]+y2[i]+.1,y2[i]) # adding text to some x,y position
plt.show()