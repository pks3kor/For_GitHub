tmp = [1,2,3,5,6,7,3,8,4,9,5,0,4,5,2,3,7]

#~ print [i for i,v in enumerate(tmp) if v==3]

cnt = 0
tmp3 = []
for i in tmp:
    if i==3:
        tmp3.append(cnt)
        cnt +=1
    else:
        cnt +=1
print max(tmp3)