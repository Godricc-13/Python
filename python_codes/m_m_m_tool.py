import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# loading the dataset
df = pd.read_csv('C:\MCA\python\python_codes/Iris.csv')

# preview data
print("Dataset Preview:")
print(df.head())

numeric_df = df.select_dtypes(include=[np.number])

# basic statistics
mean = numeric_df.mean()
median = numeric_df.median()
mode = numeric_df.mode().iloc[0]  # mode() can return multiple modes, select the first row

print("\nMean of numeric columns:\n", mean)
print("\nMedian of numeric columns:\n", median)
print("\nMode of numeric columns:\n", mode)

# plot histograms for each numeric column
for column in numeric_df.columns:
    plt.figure(figsize=(6, 4))
    plt.hist(numeric_df[column], bins=20, color='skyblue', edgecolor='black')
    plt.title(f'Histogram of {column}')
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()
