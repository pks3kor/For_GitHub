file = open("num.txt","r")
#~ print file

for line in file:
    print line
    print file.tell()

#~ with open("num.txt","r") as f:
    #~ line = f.read()
    #~ print line
    #~ print f.tell()
file.close()

