def countUpperLowerCase(tmp):
    upper = len([elem for elem in tmp if ord(elem) >=65 and ord(elem) <=90])
    lower = len([elem for elem in tmp if ord(elem) >=97 and ord(elem) <=122])
    
    return  {"lower":lower,"upper":upper}


tst = "This is FOURTH Class in leanBAY"
print countUpperLowerCase(tst)