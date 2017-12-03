tmp = iter([1,2,3])
#~ print tmp.next()
#~ print tmp.next()
#~ print tmp.next()
#~ print tmp.next()
#~ print dir(tmp)
#~ print tmp.__iter__
for i in tmp:
    print i
    #~ print next(tmp)
#~ else:
    #~ print "OK"