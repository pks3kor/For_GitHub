import re

tmp = "T2657345347s This This is learnbay class learnbay"
srchObj = re.search("(T.*s ).*(learnbay)",tmp,re.S)

print srchObj.group()
print srchObj.groups()
#~ var =srchObj.groups()
#~ if var[1] == "learnbay":
    #~ print "OK"
#~ else:
    #~ print "NOK"
