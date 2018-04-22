def chkLevel(x):
    raise Exception,"Invalid level!!!"
    print x

try:
    chkLevel(-10)
except Exception as err:
    print err