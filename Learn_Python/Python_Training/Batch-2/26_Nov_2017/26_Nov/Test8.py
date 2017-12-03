tmp5 = {
        "(A,B)":[1,2,3],
        "B":(4,),
        "C":{"T":12},
        "D":{"U":13},
        13:13
    }
#~ print tmp5.keys()
#~ print tmp5.values()
#~ print tmp5.items()
print list(tmp5.viewkeys())[0]
