import re

tmp = "111 111 111 111 111 222333444555666"
srchObj = re.search("(111 )(\\1)(\\2)\\1(\\3)",tmp)
#~ srchObj = re.search("111 ",tmp)
print srchObj.group()
#~ print srchObj.group()