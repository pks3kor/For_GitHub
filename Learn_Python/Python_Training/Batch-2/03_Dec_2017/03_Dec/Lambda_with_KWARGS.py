tmp = lambda x,y,z,**val:x+y+z+val["c"]
print tmp(1,2,3,a=4,b=5,c=6)