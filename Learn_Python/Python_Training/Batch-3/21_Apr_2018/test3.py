#~ Syntax:
#~ try:
    #~ <code here>
    #~ .
#~ except:
    #~ <statement>
#~ finally:
    #~ <statement>

a = 1
b = 0
try:
    print a/2
    print (2+"a")/0
    print 2/0
except Exception as var:
    print var
finally:
    print "OK"