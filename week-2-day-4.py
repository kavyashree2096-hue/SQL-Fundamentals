import pandas as pd
import numpy as np

# -----------------------------------
# 1. Load Dataset
# -----------------------------------
df = pd.read_csv("data4.csv")

print("Original Dataset:")
print(df.head())

print("\nDataset Shape:", df.shape)

# -----------------------------------
# 2. Check Missing Values
# -----------------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------------
# 3. Remove Duplicate Rows
# -----------------------------------
print("\nDuplicate Rows:", df.duplicated().sum())

df = df.drop_duplicates()

# -----------------------------------
# 4. Handle Missing Values
# -----------------------------------

# Numerical columns -> Median
numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Categorical columns -> Mode
categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    if df[column].isnull().sum() > 0:
        df[column] = df[column].fillna(df[column].mode()[0])

# -----------------------------------
# 5. Standardise String Values
# -----------------------------------

for column in categorical_columns:
    df[column] = df[column].astype(str).str.strip().str.lower()

# -----------------------------------
# 6. Detect Outliers using IQR
# -----------------------------------

for column in numeric_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    # Cap outliers instead of deleting useful records
    df[column] = df[column].clip(
        lower=lower_bound,
        upper=upper_bound
    )

# -----------------------------------
# 7. Save Cleaned Dataset
# -----------------------------------

df.to_csv("cleaned_dataset.csv", index=False)

# -----------------------------------
# 8. Final Data Quality Check
# -----------------------------------

print("\nAfter Cleaning:")
print("Shape:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDuplicates After Cleaning:")
print(df.duplicated().sum())

print("\nCleaned Dataset:")
print(df.head())

print("\nCleaning completed successfully!")