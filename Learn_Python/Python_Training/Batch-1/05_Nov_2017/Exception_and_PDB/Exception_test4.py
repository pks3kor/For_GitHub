def level(lev):
    assert (lev < 1), "Invalid level"
    print "i am here"

try:
    level(2)
except AssertionError as AE:
    print AE
