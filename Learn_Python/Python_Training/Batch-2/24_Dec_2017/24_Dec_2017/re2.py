import re

#~ re.search(<pattern>,<search>,<options>)

tmp = "This is \t learnbay Class"

srchObj = re.search("This .* Class",tmp,re.I)
print srchObj.group()
#~ print srchObj.groups()
