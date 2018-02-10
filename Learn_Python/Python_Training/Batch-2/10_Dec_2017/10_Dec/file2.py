#~ open(<filename>,<option>)

fh = open("Test12.txt","w")

fh.write("This is line1\n")
fh.write("This is line2\n")
fh.write("This is line3\n")
print fh.name
print fh.closed
print fh.mode
fh.close()
print fh.closed