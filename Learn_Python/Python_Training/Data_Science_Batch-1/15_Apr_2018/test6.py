import re

tmp = "This is learNbAY CLASS6"
srchObj = re.search(".*learNbAY",tmp,re.I)
print srchObj.group()
