#~ file = open(<filename>)

fh = open("test4.txt","r+")
print fh.name
#~ print fh.closed
print fh.mode
fh.close()
#~ print fh.closed