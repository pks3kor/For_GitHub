#~ open(<filename>,<option>)

fh = open("Test12.txt")

#~ with open("Test12.txt") as fh:
    #~ print fh.readline()

for line in fh:
    print line,
    
fh.close()
