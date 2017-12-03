import re

tmp = "This is Learnbay CLASS \n\n"

searchObj = re.search(r".*",tmp,re.S)
#~ print searchObj.group()

if searchObj:
    print searchObj.group()
else:
    print "No match found "