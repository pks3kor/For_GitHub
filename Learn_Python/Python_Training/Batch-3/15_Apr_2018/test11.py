import re

tmp = "111 111 111 111 222 222 "
#~ srchObj = re.search("(111 )(\\1)(\\2)(\\1)(222 )\\5",tmp)
print len(re.findall("(111 )",tmp))
#~ print dir(re)
#~ print srchObj.group()
#~ print srchObj.groups()