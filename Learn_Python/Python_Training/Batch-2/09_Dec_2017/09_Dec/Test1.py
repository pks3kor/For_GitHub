a = "test1"
b = "test2"

tmp = zip(a,b)
tmp_unzip = zip(*tmp)
print tmp_unzip
