import re

line = "This is 123LearnbayCLASS";

searchObj = re.search('\d.*', line)
if searchObj:
    print searchObj.group()
