#~ fh = open("<filename>","<mode>")
fh = open(__file__)

#~ print fh.readline()

#~ print fh.tell()
#~ fh.seek(2,0)

#~ fh.seek(-4,2)

#~ fh.seek(0,2)
#~ print fh.readline()
for line in fh:
    if line == "\n":
        pass
    else:
        print line,