a = {"A":1,"B":2,"C":3}
b = iter(a)
c = list(b)
c.sort(reverse=True)
print c
print a[c[1]]
#~ print a[b.next()]
#~ print a[b.next()]
#~ print a[b.next()]