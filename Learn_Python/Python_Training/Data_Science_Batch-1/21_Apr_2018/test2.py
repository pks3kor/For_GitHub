import sys
import numpy as np

# autostrip=1 for removing leading and trailing spaces
# dtype="|U75" is for loading all the strings as well instead making them NaN(Not a number)
df = np.genfromtxt("np_csv_read.csv",delimiter=",",dtype="|U75",autostrip=1) 
print df,"\n"
print df[:,0]
#~ print df[::-1,::-1]