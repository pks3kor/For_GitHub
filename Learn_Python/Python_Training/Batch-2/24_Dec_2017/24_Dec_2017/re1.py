import re

#~ re.match(<pattern>,<search>,<options>)
#~ re.search(<pattern>,<search>,<options>)

tmp = "This is learnbay Class"

srchObj = re.match("(this) (is)",tmp,re.I)
print srchObj.group(2)
#~ print srchObj.groups()
#~ print srchObj.group()

