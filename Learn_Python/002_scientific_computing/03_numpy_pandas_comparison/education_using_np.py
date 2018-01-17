import numpy as np

df = np.genfromtxt("education_sta.csv",delimiter=",",dtype="U75",skip_header=1)
print df
is_empty = (df == "")
df[is_empty] = "NaN"

print "--->",df