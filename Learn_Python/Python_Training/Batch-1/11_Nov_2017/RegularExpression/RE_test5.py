import re

tmp = r"123456ABCDE@#$^!"

#~ searchObj = re.search(r"\d{2,4}",tmp)

#~ if searchObj:
    #~ print searchObj.group()
#~ else:
    #~ print "No match found "
    
searchObj = re.search(r"\w{,4}",tmp)

if searchObj:
    print searchObj.group()
else:
    print "No match found "