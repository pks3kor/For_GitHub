#~ <var> = lambda <arg1>,... : <some operation>
tmp = lambda x,y,*arg,**arg1:x+y+arg[-1]+arg1["b"]

print tmp(1,2,3,4,5,a=1,b=3)
