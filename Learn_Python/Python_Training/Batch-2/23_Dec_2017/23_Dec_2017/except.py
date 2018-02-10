import logging

def div(x,y):    
    return x/y

def sum(x,y):
    return x+y


try:
    div(1,0)
except ZeroDivisionError as var:
    print var

try:
    print sum(2)
except TypeError as var:
    print var

try:
    print sum(a,2)
except NameError as var:
    print var


