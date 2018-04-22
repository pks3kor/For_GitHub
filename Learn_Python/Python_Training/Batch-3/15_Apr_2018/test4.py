import re

#~ re.S or re.DOTALL to include \n as well

tmp = "This is learnbay class"
srchObj = re.search("(LEARNbaY )(class)",tmp,re.I)
print srchObj.group()
print srchObj.group(2)
