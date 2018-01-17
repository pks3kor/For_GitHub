import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

# Load dataset
dataset = pd.read_csv("irisData.csv")
#~ print dataset

# shape
print(dataset.shape)
 	
# head
print(dataset.head(5))

# descriptions
print(dataset.describe())


