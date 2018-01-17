#
# http://www.bdnyc.org/2012/05/fitting-a-gaussian-to-your-data/
#

import numpy as np 
from scipy import stats  
import random
import matplotlib.pyplot as plt

c = 50*np.random.random()*np.random.normal(1,10,5000)
#~ print c

plt.hist(c,normed=True,color="m",align="mid")

xt = plt.xticks()[0]
xmin = min(xt)
xmax = max(xt)

lispc = np.linspace(xmin,xmax,len(c))

m,s = stats.norm.fit(c)
pdf_g = stats.norm.pdf(lispc,m,s)
#~ print pdf_g
plt.plot(lispc,pdf_g,"--r",label=True)

plt.show()