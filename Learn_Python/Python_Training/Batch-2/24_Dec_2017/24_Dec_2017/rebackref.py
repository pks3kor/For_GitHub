import re

line = "123123123123";

#~ searchObj = re.search('(123)(\\1\\1)(\\2)(\\3)', line)
searchObj = re.search('(123)(\\1\\1)+', line)
if searchObj:
    print searchObj.group()
#~ \<num>