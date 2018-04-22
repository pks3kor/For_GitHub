#~ filter(lambda,<sequence>)
#~ map(lambda,<sequence>)
#~ reduce(lambda <x,y>,<sequence>)
a = range(1,11)
f1 = lambda x:x%2==0
print filter(f1,a)
print map(f1,a)

f2 = lambda x,y:x+y
print reduce(f2,a)
