def level(lev):
    if lev < 1:
        #~ raise "Invalid_level",lev
        raise Invalid_level("Invalid value")

try:
    level(2)
except Invalid_level:
    print "I am here"
