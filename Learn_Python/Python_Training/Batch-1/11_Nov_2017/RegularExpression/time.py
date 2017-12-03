import time

fh = open("time.txt","w")
for i in range(1000):
    tmp = str(time.time())
    fh.write(tmp)
    fh.write("\n")
    time.sleep(.01)