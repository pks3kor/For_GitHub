import test1 

#~ print square(5)

# To access default value of given function
print test1.add.__defaults__

print dir(test1.add)

# To module name of given function
print test1.add.__module__ # or use "func_name"

#~ print test1.add.func_name