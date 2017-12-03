import time
start_time= time.time()
#~ """
#~ Pass by value
#~ """
#~ x = [1,2]
#~ print id(x)
#~ def fun1(x):
    #~ print id(x)
    #~ x.append(3)
    #~ return x

#~ print fun1(x[:])
#~ print x
"""
Pass by reference
"""
x = [1,2]
print id(x)
def fun1(x):
    print id(x)
    x.append(3)
    return x

print fun1(x)
print x

print("--- %s seconds ---" % (time.time() - start_time))