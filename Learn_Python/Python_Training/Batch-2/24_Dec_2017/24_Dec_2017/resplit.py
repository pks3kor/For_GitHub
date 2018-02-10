import re

line = "thisis@gmail.com";

print re.split('\W',line)
#~ if searchObj:
    #~ print searchObj.group()
help(re.split)