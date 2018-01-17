"""
Author : Pankaj soni
"""


import memory_profiler as mp

size = 10000000
#~ print help(mp.memory_usage)
print "Memory before (in MB):",mp.memory_usage()[0]

l_com = {x:x*x for x in range(size)}
print "Memory after dict compre (in MB):",mp.memory_usage()[0]

l_com = ({x:x*x} for x in range(size))
print "Memory after dict iterator (in MB):",mp.memory_usage()[0]
#~ print l_com.next()

