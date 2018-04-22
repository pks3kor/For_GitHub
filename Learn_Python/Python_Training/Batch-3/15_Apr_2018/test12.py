import re
fh = open("testfile.txt")

for line in fh:
    if line[0] == "\n":
        pass
    else:
        srchObj = re.search("(line[1]?[24680]$)",line)
        if srchObj:
            print srchObj.group(1)
    