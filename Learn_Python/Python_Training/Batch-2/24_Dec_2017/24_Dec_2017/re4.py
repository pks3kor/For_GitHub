import re

line = "This is Learnbay * CLASS\n";

searchObj = re.search( r'\*', line)
if searchObj:
    print searchObj.group()
