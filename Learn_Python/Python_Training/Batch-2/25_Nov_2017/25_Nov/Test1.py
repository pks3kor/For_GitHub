#~ [expression for <var> <seq> <if condition>]

tmp = [1,2,3,4,5]

#~ tmp2 = []
#~ for val in tmp:
    #~ tmp2.append(val*2)
#~ print tmp2

print [x for x in tmp if (x*2)%3 == 0]