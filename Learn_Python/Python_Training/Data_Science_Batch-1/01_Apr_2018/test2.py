tmp = {"A":123,"B":456,"C":789}
#~ print dir(tmp)
#~ print tmp.keys()
#~ print tmp.values()
#~ print tmp.pop(<key>)
#~ print tmp
tmp["D"] = 56456459
d2 = {"t1":123}
tmp.update(d2)
del tmp["B"]
print tmp
del tmp
print tmp