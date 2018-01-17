#
# http://www.bdnyc.org/2012/05/fitting-a-gaussian-to-your-data/
#

# Various polynomial plot andand best fit curve
import numpy as np 
from scipy import stats  
import random
import matplotlib.pyplot as plt

x = np.linspace(-200,200,100)
y = np.linspace(-4,4,100)
z = np.linspace(-4,4,100)
#~ pyt = x**3 + (2*x*y)*(z**2) - y*z + 1
#~ pyt =  x**3 - 9*x 
#~ pyt = (x - 3)*(x - 2)*(x - 1)*(x)*(x + 1)*(x + 2)
#~ pyt = x**2-x-2
pyt = (x - 3)*(x - 2)*(x - 1)*(x)*(x + 1)*(x + 2)*(x + 3)
#~ pyt =  x**4 - 4*x 
#~ pyt =  (1+2*x)/20
#~ print pyt


#~ plt.hist(pyt,normed=True,color="m",align="mid")
plt.plot(np.linspace(min(x),max(x),len(pyt)),pyt)
plt.text(x[20],pyt[20]+3,"x^3 - 9*x")

xt = plt.xticks()[0]
xmin = min(xt)
xmax = max(xt)

lispc = np.linspace(xmin,xmax,len(pyt))

m,s = stats.norm.fit(pyt)
pdf_g = stats.norm.pdf(lispc,m,s)
#~ print pdf_g
plt.plot(lispc,pdf_g,"--r",label=True)
plt.grid(True)
plt.show()