import numpy as np
tmp = np.array(((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)))
tmp = tmp.reshape(3,5)
print tmp
#~ print tmp[:,4]
#~ print tmp[1:,2]
#~ print tmp[::,::]
#~ print tmp[:,[0,1,3]]
print tmp[::-1,::-1]