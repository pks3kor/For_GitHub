import re
line = "This is Learnbay + CLASS\n";

searchObj = re.search( r'([CLASS])(earnbay).*(CLASS)', line)
print dir(searchObj)
if searchObj:
   print searchObj.group(3)
   print searchObj.start()
   print searchObj.end()
else:
   print "Nothing found!!"
