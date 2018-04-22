import re
tst = "12345,6"
h = re.compile('\d')
print h.search(tst).group()
print dir(h)