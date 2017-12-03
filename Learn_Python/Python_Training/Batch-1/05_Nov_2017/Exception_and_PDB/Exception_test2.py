def div(a,b):
    try:
        print "OK"
        print a+0
        #~ //~ print "Root cause of crash is::",var
    except (ZeroDivisionError,TypeError) as var:
        print var
div("A","B")