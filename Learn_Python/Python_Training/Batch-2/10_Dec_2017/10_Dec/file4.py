#~ open(<filename>,<option>)

fh = open("Test12.txt","r+")
print fh.tell()
print fh.readline()
fh.seek(0,1)
print fh.readline()
#~ fh.seek(0,2)
#~ print fh.readline()
fh.close()
