import numpy as np 
import matplotlib.pyplot as plt

col = ["b","g","r","c","m","k","y"]
col_dict = {"b":"--","g":"v","r":"<","c":"H","m":"p","k":"|","y":"_"}
x = np.arange(0,10*np.pi,0.1)
y = np.sin(x)


for i in range(1,8):    
    #~ print col_dict[col[i-1]]
    plt.subplot(3,3,i)
    plt.plot(x,np.sin(x+i*2),col_dict[col[i-1]]) # where -- is the line type and m for magenta color
    plt.title("Sin Wave") 
    plt.xlabel("time") 
    plt.ylabel("value") 
plt.show()