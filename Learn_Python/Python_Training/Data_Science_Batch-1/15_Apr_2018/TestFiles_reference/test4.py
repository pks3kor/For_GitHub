import re
line = "this is test $$line @@";
dig = "ABCDEF123456GHIJKL"
t1 = "111 111 111 111 AAA BBB CCC "
#~ m = re.search(r"[\w\s]*(\W)*", line)
#~ m = re.search(r"(A)", dig)
#~ m = re.search(r"(111 )\1\1\1", t1)
m = re.search(r"(111 )*(\D*)", t1)

if m:
   print m.group()
else:
   print "Nothing found!!"
