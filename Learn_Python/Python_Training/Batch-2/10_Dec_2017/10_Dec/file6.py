#~ open(<filename>,<option>)

fh = open(__file__)
#~ print __file__

#~ with open("Test12.txt") as fh:
    #~ print fh.readline()

for line in fh:
    if line == "\n":
        pass
    else:
        print line,
    
fh.close()
