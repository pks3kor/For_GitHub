#~ file = open("num1.txt","w")
#~ file = open("num1.txt","wb")
#~ file = open("num1.txt","w+")
file = open("num1.txt","wb+")
#~ print file

#~ print file.read()
#~ print file.seek(2)
file.write("ABCDE\n")
file.write("FGHIJ")
#~ print file.read()
#~ file.write("12345")
file.close()