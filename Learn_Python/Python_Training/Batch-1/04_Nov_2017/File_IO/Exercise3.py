fh = open("multiline.txt")

for line in fh:
    #~ if line == "":
    #~ if line != "":
    if line[0] != "\n":
        if int(line[-2])%2 == 0:
            print line,