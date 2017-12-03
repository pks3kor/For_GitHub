def div(a,b):
    try:
        print "OK"
        print a+0
    except (ZeroDivisionError,TypeError) as var:
        print var
    finally:
        print "Exception block has been handled"
div("A","B")