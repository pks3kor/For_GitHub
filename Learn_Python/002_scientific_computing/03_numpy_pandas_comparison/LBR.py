#~ import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("LBR.csv")

LW = df["LW"]
LD = df["LD"]
RW = df["RW"]
RD = df["RD"]
#~ print LW
#~ print LD
BAL = (LW*LD == RW*RD)
tmp = df[BAL]
plt.plot(df["LW"],df["LD"])
plt.show()