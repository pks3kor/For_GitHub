#~ open(<filename>,<option>)

fh = open("Test12.txt","w")
fh.seek(1,0)
help(fh.seek)
fh.write("This is line4\n")
fh.write("This is line5\n")
fh.write("This is line6\n")
#~ print fh.name
#~ print fh.closed
#~ print fh.mode
fh.close()
#~ print fh.closed