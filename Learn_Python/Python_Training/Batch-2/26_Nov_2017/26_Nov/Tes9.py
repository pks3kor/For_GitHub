tmp5 = {
        "(A,B)":[1,2,3],
        "B":(4,),
        "C":{"T":12},
        "D":{"U":13},
        13:13
    }
print tmp5
#~ print tmp5.has_key("DD")
#~ print "DD" in tmp5

#~ tmp6 = tmp5.copy()
#~ print tmp6

#~ print tmp5.pop("D")
print tmp5.popitem()
print tmp5.popitem()