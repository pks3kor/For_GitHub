tst = "THIS is LEArnbay CLASS"
def countLowerUpperCase(tmp):
    low_case = [elem for elem in tmp if ord(elem) >= 97 and ord(elem) <= 122]
    up_case =  [elem for elem in tmp if ord(elem) >= 65 and ord(elem) <= 90]
    print low_case
    print up_case
    #~ return {"low_case":len(low_case),"up_case":len(up_case)}
    return (low_case,up_case)
a,b = countLowerUpperCase(tst)
print a
print b