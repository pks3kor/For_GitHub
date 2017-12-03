for i in range(1,100):
    if i >1:
        for j in range(2,i):
            if i%j==0:
                #~ print "Not a prime number"
                break
        else:
            print i," is prime number"
                #~ break 