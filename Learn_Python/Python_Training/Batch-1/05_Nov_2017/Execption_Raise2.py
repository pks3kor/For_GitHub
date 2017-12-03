class ZeroDivisionError(Exception):
    def __init__(self, mismatch):
        Exception.__init__(self, mismatch)

def div(a,b):
    print a/b
    #~ raise ZeroDivisionError("dfjzhxvhzv")

#~ div(1,0)
try:
    div(1,0)
    raise ZeroDivisionError("asfasf")
except ZeroDivisionError as ZD:
    #~ pass
    print ZD
