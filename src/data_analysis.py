import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/Housing - Housing.csv")

# Display first 5 records
print("First 5 records:")
print(df.head())

# Number of rows and columns
print("\nDataset shape:")
print(df.shape)

# Column names
print("\nColumn names:")
print(df.columns)

# Dataset information
print("\nDataset information:")
df.info()

# Statistical summary
print("\nStatistical summary:")
print(df.describe())

# Missing values
print("\nMissing values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate rows:", df.duplicated().sum())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)

# Data types
print("\nData types:")
print(df.dtypes)

# Check missing values again
print("\nMissing values after cleaning:")
print(df.isnull().sum())