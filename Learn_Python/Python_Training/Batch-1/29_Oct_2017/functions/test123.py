#~ tmp = "This is Python Class and TODAYS day is SUNday"

upper_cnt = 0
lower_cnt = 0


def filterUperLowercase(statement):
    global upper_cnt
    global lower_cnt
    #~ upper_cnt = 0
    #~ lower_cnt = 0
    for itm in statement:
        tmp4 = ord(itm)
        if tmp4 >=65 and tmp4 <=90:
            upper_cnt +=1
        elif tmp4 >=97 and tmp4 <=122:
            lower_cnt +=1
    return{"upper_cnt":upper_cnt,"lower_cnt":lower_cnt}

tmp = raw_input("Please give your statement.....")
print filterUperLowercase(tmp)
