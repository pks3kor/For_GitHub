import re

#~ line = "1234567890";

#~ searchObj = re.search( r'.', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ searchObj = re.search( r'.*', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ searchObj = re.search( r'[aA-zZ0-9]*', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ searchObj = re.search( r'.?', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ searchObj = re.search( r'^123', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ searchObj = re.search( r'90$', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ searchObj = re.search( r'\d', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ line = "1234567890";
#~ searchObj = re.search( r'(\d){3}', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ searchObj = re.search( r'(\d){2,5}', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ searchObj = re.search( r'(\d){,}', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ searchObj = re.search( r'(\d){3,}', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ searchObj = re.search( r'(\d){,5}', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ line = "123 ABC";
#~ searchObj = re.search( r'(123)|(ABC)|(EFG)', line)
#~ print "search --> searchObj.group() : ", searchObj.groups()

#~ line = "123ABC ";
#~ searchObj = re.search( r'\d\d\d', line)
#~ print "search --> searchObj.group() : ", searchObj.group()
#~ searchObj = re.search( r'\D\D\D', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ line = "pankaj@#$!"
#~ searchObj = re.search( r'\W+', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

#~ line = "1234 \r\n"
#~ searchObj = re.search( r'\d{4}\s{3}', line)
#~ print "search --> searchObj.group() : ", searchObj.group()

line = "1234AB\r\n"
searchObj = re.search( r'1234\S', line)
print "search --> searchObj.group() : ", searchObj.group()
