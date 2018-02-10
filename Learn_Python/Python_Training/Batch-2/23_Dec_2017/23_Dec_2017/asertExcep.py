def div(x,y):
    assert (y!=0),"ZeroDivision error"
    return (x/y)

#~ print div(1,2)
try:
    print div(2,0)
except AssertionError as var:
    print var