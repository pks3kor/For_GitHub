import re

tmp = r"123123123456567"
    
searchObj = re.search(r"(123)+?",tmp)

if searchObj:
    print searchObj.group()
else:
    print "No match found "