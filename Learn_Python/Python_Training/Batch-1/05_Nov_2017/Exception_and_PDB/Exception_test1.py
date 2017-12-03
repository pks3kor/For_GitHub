def div(a,b):
    try:
        print a/b
    except (ZeroDivisionError,TypeError) as var:
        print "Root cause of crash is::",var

div(1,0)