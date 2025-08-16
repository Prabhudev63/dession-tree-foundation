# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt
import warnings

# Ignore warnings
warnings.filterwarnings("ignore")

# Load dataset
df = pd.read_csv(r"C:\a247\1st_ML\dession-tree-foundation\breast_cancer_data.csv")

# Show first and last rows
print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

# Show shape (rows, columns)
print("\nShape of dataset:")
print(df.shape),
df.shape[0],
df.columns
df.info()

print("-"*500)

Print(df.describe())

print(df.isnull().sum())

