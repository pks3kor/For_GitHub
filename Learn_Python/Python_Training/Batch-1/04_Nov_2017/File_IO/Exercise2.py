fh = open(__file__)
print fh.name
cnt = 1
for line in fh:
    print "Line number::",cnt,line,
    cnt +=1