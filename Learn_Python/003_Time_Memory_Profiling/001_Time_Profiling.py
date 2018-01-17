"""
Author : Pankaj soni
"""

import time
#~ print time.time()

t1 = time.time()
size = 10000000
l_com = ({x:x*x} for x in range(size))
print "Time taken for dict iterator in Seconds",time.time()-t1
#~ print l_com.next()

t1 = time.time()
l_com = {x:x*x for x in range(size)}
#~ print l_com
print "Time taken for dict creation in Seconds",time.time()-t1