import re

tmp = "This is learNbAY CLASS6"
#~ tmp = "ABCDEFAB"
#~ matchObj = re.match("AB",tmp)
matchObj = re.match("This (is)",tmp)
print matchObj.group()
print matchObj.groups()
