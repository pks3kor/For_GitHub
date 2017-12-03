tmp = "This is Python Class and TODAYS day is SUNday"
upper = 65
lower = 97


def filterUperLowercase(statement):
    upper_cnt = 0
    lower_cnt = 0
    tmp = statement.split()
    #~ print tmp
    for itm in tmp:
        #~ print itm
        for chr in itm:
            #~ print chr
            tmp4 = ord(chr)
            if tmp4 >=65 and tmp4 <=90:
                upper_cnt +=1
                #~ print upper_cnt
            elif tmp4 >=97 and tmp4 <=122:
                lower_cnt +=1
                #~ print lower_cnt
    return (upper_cnt,lower_cnt)
    
print filterUperLowercase(tmp)
