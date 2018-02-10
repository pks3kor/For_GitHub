import logging

def div(x,y):    
    return x/y

def sum(x,y):
    return x+y


try:
    print div(1,2)
except ZeroDivisionError as var:
    print var