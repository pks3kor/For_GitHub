#~ file = open("num.txt","r")
#~ file = open("num.txt","rb")
#~ file = open("num.txt","r+")
file = open("num.txt","rb+")
#~ print file

print file.read()
#~ print file.seek(2)
#~ file.write("ABCDE")
#~ print file.read(5)
#~ file.write("12345")
file.close()