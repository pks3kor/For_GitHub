import re

line = "This is Learnbay Class";

# For matching
matchObj = re.match( r'Learnbay', line)
if matchObj:
   print "match --> matchObj.group() : ", matchObj.group()
else:
   print "No match!!"


# For searching
searchObj = re.search( r'Learnbay', line)
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"


# For substituting
line = "This is Learnbay Learnbay Learnbay Class";

print re.sub(r'Learnbay', "LB", line);
print re.sub(r'Learnbay', "LB", line,1);
print line

# To match meta characters
line = "This is Learnbay + Class";

searchObj = re.search( r'\+', line)
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"


# Using flags
line = "This is Learnbay + CLASS\n";

searchObj = re.search( r'class.', line,re.I|re.S) # I= case insensitive, S = match any char including new line
if searchObj:
   print "search --> searchObj.group() : ", searchObj.group()
else:
   print "Nothing found!!"
