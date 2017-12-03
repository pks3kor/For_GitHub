import re

line = "This is Learnbay class1 class2 class3";

searchObj = re.search( r'(class[0-9]).*?', line)
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"
