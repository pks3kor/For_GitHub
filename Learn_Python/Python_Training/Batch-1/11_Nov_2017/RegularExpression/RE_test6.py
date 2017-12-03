import re

tmp = r"345123456ABCDE@#$^!"
    
searchObj = re.search(r"(56A|BCD)",tmp)

if searchObj:
    print searchObj.group()
else:
    print "No match found "