import re
line = "testAbcNY@learnbay.in@gmail.com"

srchObj = re.search("((\w)+@(\w)+\.[a-z]{2,})$",line)
if srchObj:
    #~ print line,
    print srchObj.group()
