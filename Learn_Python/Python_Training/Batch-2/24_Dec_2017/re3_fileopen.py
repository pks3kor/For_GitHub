import re

fh = open("text.txt")

line = "soni.pankajku123mar@gmail.com"

cnt = 0
cnt2 = 0
for line in fh:
    tmp = line
    #~ print tmp
    srchObj = re.search("\d$",tmp)
    srchObj2 = re.search("^\n",tmp)
    if srchObj:
        #~ print line
        cnt +=1
        #~ print srchObj.group()
    elif srchObj2:
        #~ print line
        cnt2 +=1
print cnt
print cnt2    


#~ tmp = re.split("\d+",line)

#~ print "".join(tmp)
#~ if srchObj:
    #~ print line
    #~ print srchObj.group(1)

#~ print re.sub("\d*","",line)