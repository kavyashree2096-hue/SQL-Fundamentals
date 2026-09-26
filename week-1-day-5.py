import pandas as pd

# 1. Create sample data
data = {
    "Name": ["Kavya", "Rahul", "Ananya", "Arjun", "Sneha", "Ravi", "Priya", "Kiran"],
    "Department": ["Sales", "IT", "Sales", "HR", "IT", "Sales", "HR", "IT"],
    "Age": [21, 23, 22, 25, None, 24, 22, 26],
    "Salary": [30000, 45000, 35000, 40000, 50000, None, 38000, 55000],
    "City": ["Bangalore", "Mysore", "Bangalore", "Chennai", "Mysore", "Bangalore", None, "Chennai"]
}

df = pd.DataFrame(data)

# 2. Save data to CSV
df.to_csv("sales_data.csv", index=False)

# 3. Load CSV
df = pd.read_csv("sales_data.csv")

print("Original Data:")
print(df)

# 4. Inspect data
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nDepartment Counts:")
print(df["Department"].value_counts())

# 5. Select columns
print("\nSelected Columns:")
print(df[["Name", "Department", "Salary"]])

# 6. Filter rows
print("\nSalary Above 40000:")
print(df[df["Salary"] > 40000])

# 7. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 8. Handle missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
df["City"] = df["City"].fillna("Unknown")

print("\nAfter Handling Missing Values:")
print(df)

# 9. Group by Department
print("\nAverage Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

print("\nTotal Salary by Department:")
print(df.groupby("Department")["Salary"].sum())

print("\nEmployee Count by Department:")
print(df.groupby("Department")["Name"].count())

# 10. Export cleaned data
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned data exported successfully!")