import re
fh = open("email.txt")

for line in fh:
    srchObj = re.search("(\w)+@(\w)+\.[a-z]{2,}",line)
    #~ print line,
    if srchObj:
        print line,
        print srchObj.group()
    