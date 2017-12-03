#~ file = open(<filename>)
# r,rb,r+,rb+
fh = open("test.txt","r+")
print fh.read()

#~ for line in fh:
    #~ print line

#~ fh.write("This is test2")
fh.close()