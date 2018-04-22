fh = open("testfile.txt")
#~ print fh.read()
data = []
for line in fh:
    if line[0] == "\n":
        pass
    elif int(line[-2])%2==0:
        data.append(line)
#~ TBD::
#~ try:
    #~ fh.write(data)
#~ except IOError:
    #~ fh.close()
    #~ fh = open("testfile.txt","w")
    #~ fh.write()