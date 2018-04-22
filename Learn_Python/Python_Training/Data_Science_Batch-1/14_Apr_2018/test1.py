def checkLevel(x,y):
    assert(x>10),"Invalid Level!!!"
    print "i am after assert"
    return x+y

def checkLevel2(x,y):
    if x>10:
        raise Exception("Invalid Level!!!")
        print "OK"
    print "i am after raise"
    return x+y

try:
    checkLevel(20,3)
except AssertionError as err:
    print err
finally:
    print "i m in finally block"
    
try:
    checkLevel2(20,3)
except (AssertionError,Exception) as err:
    print err