import re

tmp = "111222333444555666ABCDEFAB"
#~ srchObj = re.search("(\d*)(\D*)(.)",tmp,re.I)
srchObj = re.search("(AB).*(AB)",tmp,re.I)
print srchObj.pos
#~ print dir(srchObj)
#~ print srchObj.start()
#~ print srchObj.end()
#~ print srchObj.group(3)
#~ print srchObj.groups()
