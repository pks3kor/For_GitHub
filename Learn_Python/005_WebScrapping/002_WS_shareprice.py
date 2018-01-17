import urllib
import re
import time
from bs4 import BeautifulSoup

web= "https://in.finance.yahoo.com/quote/AAPL?p=AAPL"


for trial in range(100):
    htmlfile = urllib.urlopen(web)
    htmltext = htmlfile.read()
    soup = BeautifulSoup(htmltext, 'html.parser')
    
    #~ print soup.prettify("latin-1")
    
    #~ print soup.find_all("span")
    #~ print soup.prettify("latin-1")
    a = "<span class=\"Trsdu\(0\.3s\) Trsdu\(0\.3s\) Fw\(b\) Fz\(36px\) Mb\(-4px\) D\(b\)\" data-reactid=\"14\"><!-- react-text: 15 -->(.+)?<!-- /react-text --></span>"
    srch = re.compile(a)
    for itm in soup.find_all("span"):
        #~ print itm
        mObj = re.search(srch,str(itm))
        if mObj:
            print "trial number::%d and share price is %s "%(trial,mObj.group(1))
    time.sleep(1)
    
