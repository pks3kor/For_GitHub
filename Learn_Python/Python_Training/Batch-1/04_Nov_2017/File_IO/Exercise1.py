fh = open("test2.txt")

cnt = 1
for line in fh:
    print "Line number::",cnt,line
    cnt +=1