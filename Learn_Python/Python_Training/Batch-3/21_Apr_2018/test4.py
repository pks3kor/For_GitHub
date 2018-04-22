def chkLevel(x):
    assert(x>0),"Invalid level!!!"
    print x

#~ chkLevel(10)
#~ chkLevel(-10)

try:
    chkLevel(-10)
except AssertionError as err:
    print err