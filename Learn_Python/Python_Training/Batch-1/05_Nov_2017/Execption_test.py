a = 1
b = 2
c = "Test1"
#~ print a/0
try:
    print a/0
    #~ print b+c
    #~ print "I am here"
except (ZeroDivisionError,TypeError) as ZD   :
    print ZD
finally:
    print "Exception has been handled"
