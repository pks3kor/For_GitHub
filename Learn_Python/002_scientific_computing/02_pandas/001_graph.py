import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Line
#~ df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
   #~ periods=10), columns=list('ABCD'))

# Bar
#~ df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])

# Box
#~ df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])

# Area
#~ df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])

#~ # Histogram
#~ df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

# Pie
df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])

#~ df.plot() #Line
#~ df.plot.bar() #Bar
#~ df.plot.bar(stacked=True) # Stacked
#~ df.plot.barh(stacked=True) #Bar hori
#~ df.plot.hist(bins=20) # Histogram
#~ df.plot.box() # Box
#~ df.plot.area() # Area
#~ df.plot.scatter(x='a',y='b') # Scatter
df.plot.pie(subplots=True) # Pie

plt.show()