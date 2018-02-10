import time


fh = open("test2.txt","w")

for i in range(1000):
    tmp = time.time()
    print tmp
    fh.write(str(tmp)+"\n")
    time.sleep(.017)
fh.close()