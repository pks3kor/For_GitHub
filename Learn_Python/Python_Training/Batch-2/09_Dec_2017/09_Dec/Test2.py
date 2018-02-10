#~ tmp = lambda <var>:<expr>

#~ tmp = lambda x,y:x+y
#~ print tmp(2,3)

tmp = range(50)
#~ print tmp
func = lambda x:x%2==0
#~ print func(2)
#~ filter(<lambda>,<seq>)
#~ map(<lambda>,<seq>)
#~ reduce(<lambda>,<seq>)

#~ print filter(func,tmp)
#~ print map(func,tmp)
print reduce(func,tmp)