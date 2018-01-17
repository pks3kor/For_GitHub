"""
Author : Pankaj soni
"""

# function with yield KW will create an iterator
def sum(tmp):
    """
    without yield
    """
    while tmp >=0:
        print tmp
        tmp -=1

def sum1():
    """
    with yield
    """
    while 1:
        tmp = yield
        yield tmp

#~ print sum(1) # return all value
#~ print sum1() # return generatroe object
s = sum1()
s.next()
s.send("asff")
s.send(123)
print s.send([1,2,3])
#~ print s.next()