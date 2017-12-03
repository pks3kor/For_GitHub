import os
file = open(__file__,"r")
#~ print __file__

for line in file:
    print line[0:-1]
    #~ print file.next()
    #~ print file.next()
#~ print file.tell()
#~ file.seek(0,1)
#~ file.write("PANKAJjfczxadf")
#~ print file.name
#~ print file.mode
#~ print file.closed
#~ file.close()
#~ print file.closed
#~ os.remove("num_bkp.txt")

#~ os.chdir("C:\\")
#~ print os.getcwd()