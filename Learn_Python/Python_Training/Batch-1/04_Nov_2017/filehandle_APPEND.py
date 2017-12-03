#~ file = open("num1.txt","a")
#~ file = open("num1.txt","ab")
#~ file = open("num1.txt","a+")
file = open("num1.txt","ab+")
#~ print file

print file.read()
#~ print file.seek(2)
#~ file.write("\n12345")
#~ file.write("FGHIJ")
#~ print file.read()
#~ file.write("12345")
file.close()