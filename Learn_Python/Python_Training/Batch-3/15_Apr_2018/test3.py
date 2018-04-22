import re

#~ re.S or re.DOTALL to include \n as well

tmp = "This is learnbay class"
srchObj = re.search("LEARNBAY",tmp,re.I)
print srchObj.group()