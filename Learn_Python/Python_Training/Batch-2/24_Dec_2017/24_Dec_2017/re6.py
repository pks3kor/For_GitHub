import re

line = "This is learnbay class";

searchObj = re.search('class$', line)
if searchObj:
    print line
    print searchObj.group()