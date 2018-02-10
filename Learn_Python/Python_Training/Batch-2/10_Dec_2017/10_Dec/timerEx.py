import time

fh = open("testtime.txt","w")
for i in range(1000):
    tmp = time.time()
    fh.write(str(tmp)+"\n")
    print tmp
    time.sleep(.01)
    