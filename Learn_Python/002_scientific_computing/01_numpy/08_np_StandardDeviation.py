"""
Author : Pankaj soni

Standard Deviation:
1. Work out the Mean (the simple average of the numbers)
2. Then for each number: subtract the Mean and square the result
3. Then work out the mean of those squared differences.
4. Take the square root of that and we are done!
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array([9,2,5,4,12,7,8,11,9,3,7,4,12,5,4,10,9,6,9,4],dtype=np.float64)
#~ y = np.array([4,6,6.5,2.3,6.3,2.8,3.2,7],dtype=np.float64)

x_mean = np.mean(x)
print x_mean
#~ print np.std(x)
sub_sq = [(tmp-x_mean)**2 for tmp in x]
print sub_sq
sub_sq_mean =  np.mean(sub_sq)
print sub_sq_mean
sqrt_sub_sq_mean = np.sqrt(sub_sq_mean)
print sqrt_sub_sq_mean

diff = [sqrt_sub_sq_mean+elem for elem in x]
print diff
plt.scatter(x,x)
plt.plot(x,diff)
plt.show()