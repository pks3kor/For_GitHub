import re

tmp = "T2657345347s This This is learnbay class"
srchObj = re.search("LEARNBAY|learnbay",tmp)

print srchObj.group()