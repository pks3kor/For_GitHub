def div(x,y):
    assert (y!=0),"Division by zero error!!!"
    return x/y

#~ print div(4,0)
try:
    print div(4,0)
except AssertionError as e:
    print e
    