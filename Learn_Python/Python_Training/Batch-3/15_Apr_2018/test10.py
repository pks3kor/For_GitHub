import re

tmp = "111222CD3 33444555ABC"
#~ srchObj = re.search("(\d*)(\D\D)(\d*)(\D*)",tmp)
srchObj = re.search("([0-9]*)([A-Z]{2})\d\s(\d*)(\D*)",tmp)
print srchObj.groups()