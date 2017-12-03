import re

# + ? . * ^ $ ( ) [ ] { } | \

tmp = r"This is Lear\nbay CLASS"

searchObj = re.search(r"Lear\\nbay",tmp)

if searchObj:
    print searchObj.group()
else:
    print "No match found "