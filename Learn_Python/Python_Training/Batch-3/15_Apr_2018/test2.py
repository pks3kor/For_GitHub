import re

tmp = "This is learnbay class"
#~ matchObj = re.match("learnbay",tmp)
matchObj = re.match("(This )(is)",tmp)
print matchObj.group()
print matchObj.groups()