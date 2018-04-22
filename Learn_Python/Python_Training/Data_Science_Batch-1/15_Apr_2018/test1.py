def test():
    return "Assertion Exception raised"
    
def checlLevel(x):
    assert(x>0),test()
    print "x is greater tan 0"

try:
    checlLevel(-1)
except AssertionError as tmp:
    print tmp