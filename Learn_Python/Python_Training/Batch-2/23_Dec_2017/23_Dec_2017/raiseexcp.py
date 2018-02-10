def levelchk(lvl):
    if lvl >0:
        raise NameError("Invalid level!!")
    print "Ok"
    print "Ok2"

#~ levelchk(1)
try:
    levelchk(1)
except NameError as var:
    print var
    