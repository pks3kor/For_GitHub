database = [
            ["Name1",1,"class-1"],
            ["Name2",2,"class-2"],
            ["Name3",3,"class-3"],
            ["Name4",4,"class-4"],
            ["Name5",5,"class-5"],
            ]

#~ print database
tmp = input("Please enter Student name::\n")
#~ print tmp
#~ print str(tmp)
#~ if tmp in database[0][0]:
    #~ print database[0]
    
for i in database:
    if tmp in i:
        print i