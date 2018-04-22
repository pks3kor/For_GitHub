#~ import <lib name>
#~ import <lib name> as <new name>
#~ from <lib name> import *
#~ from <lib name> import <f1>,f2,....

def sum(x,y):
    """
    This is sum function.
    Syntax :
        example:sum(1,2)
    """
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    z = 1
    print locals()
    return x*y

print __name__
if __name__ == "__main__":
    #~ print sum(1,2)
    print mul(2,3)