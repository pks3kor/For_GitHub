import numpy as np 
import matplotlib.pyplot as plt

x = np.arange(1,11)
y1 = 2*x+5
y2 = 2*x+1.2
y3 = 2*x+3.2
y4 = 2*x+1.67
y5 = 2*x+3.53
y6 = 2*x+4.53
y7 = 2*x+8.53
y8 = 3.9*x+2.53
y9 = 4.11*x+3.53
y10 = 5.9*x+6.53

#~ print y

plt.plot(x,y1,"-b") # where -- is the line type and m for magenta color
plt.plot(x,y2,"--g") # where -- is the line type and m for magenta color
plt.plot(x,y3,"-.r") # where -- is the line type and m for magenta color
plt.plot(x,y4,":c") # where -- is the line type and m for magenta color
plt.plot(x,y5,"om") # where -- is the line type and m for magenta color
plt.plot(x,y6,"vy") # where -- is the line type and m for magenta color
plt.plot(x,y7,"<k") # where -- is the line type and m for magenta color
plt.plot(x,y8,">g") # where -- is the line type and m for magenta color
plt.plot(x,y9,"1m") # where -- is the line type and m for magenta color
plt.plot(x,y10,"2m") # where -- is the line type and m for magenta color
plt.title("Matplotlib demo") 
plt.xlabel("x axis caption") 
plt.ylabel("y axis caption") 
plt.show()