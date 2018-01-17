#~ import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("unrate.csv")
#~ print df[0:12]
#~ print df.head(12)
df['DATE'] = pd.to_datetime(df['DATE'])
print df['DATE']
#~ print df.head(12)
#~ year = df["DATE"].head(12)
#~ data = df["UNRATE"].head(12)
#~ print year
#~ print data
fst_twelve = df[0:12]
#~ print df[:,1]
plt.plot(fst_twelve['DATE'],fst_twelve['UNRATE'])
plt.xticks(rotation=90)
plt.xlabel("TimeYear")
plt.ylabel("UNRATE")
plt.title("Unemployment Rate")
plt.show()