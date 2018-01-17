#~ import numpy as np
import pandas as pd

df = pd.read_csv("food_consume.csv")
#~ food_consume  = np.genfromtxt("food_consume.csv",delimiter=",",dtype="U75",skip_header =1)
#~ print df.size
#~ print df.head()
#~ print df.head(20)
#~ print df.shape
#~ print df.loc[[2,5,10]]
tmp = df.loc[0]
tmp2 = df.columns.values
#~ print df.columns
gram_data = []
for data in df.columns:
    if "(g)" in data:
        gram_data.append(data)
        #~ print df[data]
print gram_data
print df[gram_data]