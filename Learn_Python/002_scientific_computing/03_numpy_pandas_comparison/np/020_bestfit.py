#
# http://www.bdnyc.org/2012/05/fitting-a-gaussian-to-your-data/
#

import numpy as np 
from scipy import stats  
import random
import matplotlib.pyplot as plt

c = 50*np.random.rand() * np.random.normal(10, 10, 100) + 20

plt.hist(c, normed=True,color="y",align='mid') 

# get xticks min and max for normal distribution curve
xt = plt.xticks()[0]
xmin,xmax= np.min(xt),np.max(xt)
lnspc = np.linspace(xmin, xmax, len(c))

# lets try the normal distribution first
m, s = stats.norm.fit(c) # get mean(mu) and standard deviation(sigma)  
pdf_g = stats.norm.pdf(lnspc, m, s) # now get theoretical values in our interval  
plt.plot(lnspc, pdf_g,"--b",label="Norm") # plot it
plt.title("histogram") 
#~ plt.grid(True)
plt.show()