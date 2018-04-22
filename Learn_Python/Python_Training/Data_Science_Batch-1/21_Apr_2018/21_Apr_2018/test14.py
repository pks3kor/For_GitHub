import numpy as np
#~ a1	a2	a3	a4	a5
#~ 1	2	3	4	5
#~ b1	 b2 	b3 	b4	 b5 

csv = np.genfromtxt("np_csv_read.csv",delimiter=",")
print csv
print csv.shape
print csv.dtype
print csv.size
print csv[0]