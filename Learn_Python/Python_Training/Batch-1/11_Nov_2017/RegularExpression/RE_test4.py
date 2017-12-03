import re

fh = open("time.txt")

for line in fh:
    searchObj = re.search(r"(24)(58)\.(5)\3",line)
    if searchObj:
        #~ print searchObj.group(1)
        #~ print searchObj.group(2)
        print searchObj.groups()
        #~ print line,
