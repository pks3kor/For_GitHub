tmp = [1,2,3,4,5,6,7,8,9]
tmp2 = tmp[::-1]
print list(set([tmp[i]*tmp2[i] for i,v in enumerate(tmp) if (tmp[i]*tmp2[i])%2==0]))
print [tmp[i]*tmp2[i] for i,v in enumerate(tmp)]