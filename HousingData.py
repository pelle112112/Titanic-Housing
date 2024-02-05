import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets, preprocessing, metrics
from scipy import stats

# Reading csv file
df = pd.read_csv('house-data.csv')

print(df.head)
print(df.shape)
print(df.columns)
print(list(df))

# Checking for missing values
print(df.isnull().sum())
print(pd.isnull(df))

#Found 0 missing values
print("Current numbers of data: \n", df.count())

#Checking for outliers
df_new = df[(np.abs(stats.zscore(df.sqft_living)) < 10)]
print(df)
print(df_new)



