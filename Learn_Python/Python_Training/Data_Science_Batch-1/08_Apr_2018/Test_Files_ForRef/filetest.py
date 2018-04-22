import os
#~ fh = open("testinput1.py","a+")

#~ print fh.next()
#~ fh.write("\n123\n")
#~ print fh.next()
#~ print fh.next()
#~ fh.write("456\n")
#~ print fh.next()
#~ fh.close()

print os.getcwd()
with open("testinput.py","r") as fh:
    print fh.read()
print fh.closed