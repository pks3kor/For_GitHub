tmp = {"A":123,"B":456,"C":789,"D":342,"E":67876}
a = tmp.keys()
a.sort()
print a
print tmp[a[2:5][0]]
    
tmp = [1,2,3,2,2,2,3,4,5,5,666,2]
print list(set(tmp))[0]
