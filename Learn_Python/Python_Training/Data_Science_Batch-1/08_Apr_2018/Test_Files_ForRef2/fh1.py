fh = open("filetest.txt","r")
#~ print fh
#~ print dir(fh)
print fh.read()
print fh.closed
fh.close()
print fh.closed