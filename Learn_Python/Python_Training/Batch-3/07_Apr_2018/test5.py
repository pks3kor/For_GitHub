def sum(x,y,*arg,**arg1):
    print x
    print y
    print arg
    print arg1["a"]

sum(1,2,3,4,5,a=1,b=3,c=4)