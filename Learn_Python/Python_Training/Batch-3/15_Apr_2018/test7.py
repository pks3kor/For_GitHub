import re

tmp = "T265734\n5347s This This is learnbay class"
#~ srchObj = re.search("T.*?s",tmp)
srchObj = re.search("T.*s",tmp,re.S)

print srchObj.group()
