#~ import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
df = pd.read_csv("education_sta.csv")

#~ print df["English"]

#~ sns.kdeplot(df["English"],shade=True)
#~ sns.set_style("darkgrid")
#~ plt.show()

# Condition on unique values of the "Survived" column.
g = sns.FacetGrid(df, col="survivied", row="survivied2",size=3)
# For each subset of values, generate a kernel density plot of the "Age" columns.
g.map(sns.kdeplot, "Education", shade=True)
#~ sns.despine(left=True, bottom=True)
plt.show()