#~ import re
#~ line = "123123123123"
#~ srchObj = re.search("(\d\d\d)(\\1)\\2",line)
#~ if srchObj:
    #~ print line
    #~ print srchObj.group()
import re
line = "This is Pankaj @# Pankaj"
srchObj = re.search("Pankaj\Z",line)
if srchObj:
    #~ print line
    print srchObj.group()