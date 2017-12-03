#~ file = open(<filename>)

fh = open("test4.txt","r+")
print fh.read()
fh.seek(20)
fh.write("this is using write")
fh.close()