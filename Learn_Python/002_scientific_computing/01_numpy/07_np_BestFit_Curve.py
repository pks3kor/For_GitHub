"""
Author : Pankaj soni

m = (X^.Y^-(XY)^)/((X^)**2-X**2^)
y^ = mx^+b
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.array([2,3,7,3,8,0.9,1,9],dtype=np.float64)
y = np.array([4,6,6.5,2.3,6.3,2.8,3.2,7],dtype=np.float64)

def best_filt_line(a,b):
    m = (np.mean(x)*np.mean(y) - np.mean(x*y))/( np.mean(x)**2 - np.mean(y**2))
    b = np.mean(y)-m*np.mean(x)
    return m,b

m,b = best_filt_line(x,y)

regression_line = [(m*tmp)+b for tmp in x]
#~ print regression_line
predict_x = 10
predict_y = m*predict_x+b

plt.scatter(x,y)
plt.scatter(predict_x,predict_y,color="red")
plt.plot(x,regression_line)
plt.show()