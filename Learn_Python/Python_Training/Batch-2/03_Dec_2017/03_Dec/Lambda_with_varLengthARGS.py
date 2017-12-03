#~ lambda <var>:<expr>
tmp = lambda x,y,z,*val:x+y+z+val[0]
print tmp(1,2,3,4,5,6)

