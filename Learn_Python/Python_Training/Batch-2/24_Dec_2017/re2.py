import re
line = "soni.pankajku123mar@gmail.com"
srchObj = re.search(".*(\W)+.*",line,re.S)

#~ tmp = re.split("\d+",line)

#~ print "".join(tmp)
if srchObj:
    #~ print line
    print srchObj.group(1)

#~ print re.sub("\d*","",line)