#~ import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("education_sta.csv")

#~ print df.columns[1:]

fig = plt.figure()
plt_num = 1
cb_dark_blue = (100/255,107/255,164/255)
cb_orange_blue = (255/255,128/255,14/255)

#~ print df["Year"].iloc[-5]

for subj in df.columns[1:7]:
    ax = fig.add_subplot(2,3,plt_num)
    ax.plot(df["Year"],df[subj],c="orange",label="women",linewidth=2)
    ax.text(df["Year"].iloc[-10], df[subj].iloc[-10]+1, "women")
    ax.plot(df["Year"],100-df[subj],c="blue",label="men",linewidth=2)
    ax.text(df["Year"].iloc[-10], 100-df[subj].iloc[-10]+1, "men")
    #~ ax.set_ylim(0,100)
    #~ plt.xlabel("Year")
    #~ plt.ylabel("degrees")
    #~ plt.xticks(rotation=45)
    #~ plt.yticks(rotation=45)
    #~ ax.tick_params(bottom="off", top="off", left="off", right="off")
    plt.title("Men,Women "+subj+" Degrees")
    
    plt_num +=1
    
#~ plt.legend(loc='upper right')    
plt.show()