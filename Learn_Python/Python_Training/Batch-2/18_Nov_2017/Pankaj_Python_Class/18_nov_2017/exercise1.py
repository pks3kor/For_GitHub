import sys
#~ a = sys.argv[1:]
myFavnum = 11
for var in sys.argv[1:]:
    var = (int(var))
    if var >0 and var == 11:
        print "+ve number and my hav num"
    elif var <0 and var == 11:
        print "-ve number"
    elif var == 0 and var == 11:
        print "ZERO number"
    elif var == 11:
        print "This is my fav number"