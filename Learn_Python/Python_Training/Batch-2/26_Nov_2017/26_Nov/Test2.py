a = [1,2,333,"Test1","A","B",22343,"sjdfhsdfsdh"]
#~ print max(a)
print(max([i for i in a if isinstance(i,int)]))