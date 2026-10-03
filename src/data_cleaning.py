import pandas as pd

# Load dataset
df = pd.read_csv("../dataset/Housing - Housing.csv")

print("Original shape:", df.shape)

# Remove duplicate rows
df = df.drop_duplicates()

print("Shape after removing duplicates:", df.shape)

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Convert categorical columns to lowercase
categorical_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea",
    "furnishingstatus"
]

for column in categorical_columns:
    df[column] = df[column].str.lower().str.strip()

print("\nCleaned data:")
print(df.head())

# Save cleaned dataset
df.to_csv("../dataset/cleaned_house_prices.csv", index=False)

print("\nCleaned dataset saved successfully!")