import urllib
import re
import time
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

web= "https://in.finance.yahoo.com/quote/TIDEWATER.NS?p=TIDEWATER.NS"

sPrice = np.array([0])
xt = np.arange(0,8000)
#~ print xt
yt = np.arange(0,8000,dtype=float)
#~ print yt
#~ yt = np.insert(yt,0,100)
#~ print yt

plt.ion()    
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(xt, yt, 'r-') # Returns a tuple of line objects, thus the comma


for trial in range(100):    
    htmlfile = urllib.urlopen(web)
    htmltext = htmlfile.read()
    soup = BeautifulSoup(htmltext, 'html.parser')
    a = "<span class=\"Trsdu\(0\.3s\) Trsdu\(0\.3s\) Fw\(b\) Fz\(36px\) Mb\(-4px\) D\(b\)\" data-reactid=\"14\"><!-- react-text: 15 -->(.+)?<!-- /react-text --></span>"
    srch = re.compile(a)
    for itm in soup.find_all("span"):
        mObj = re.search(srch,str(itm))
        if mObj:
            #~ print "trial number::%d and share price is %s "%(trial,mObj.group(1))
            yt = np.insert(yt,trial,"".join(mObj.group(1).split(",")))
            #~ print yt
            #~ sPrice = np.append(sPrice,"".join(mObj.group(1).split(",")))
            #~ print yt
            for val in yt:
                line1.set_ydata(val)
                fig.canvas.draw()