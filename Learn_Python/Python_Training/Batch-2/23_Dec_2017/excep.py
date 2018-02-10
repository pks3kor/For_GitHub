def sum(x,y):
    print "a"+x
    return x/y

#~ print sum(1,0)

try:
    print sum(1,0)
except (ZeroDivisionError,TypeError) as e:
    print e
finally:
    print "OK"