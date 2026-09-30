# ============================================================
# WEEK 2 - DAY 3 : COMPLETE EDA WORKFLOW
# Exploratory Data Analysis
# ============================================================

# ------------------------------------------------------------
# 1. IMPORT LIBRARIES
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display settings
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 100)

# Plot style
sns.set_theme(style="whitegrid")


# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

# CHANGE THIS TO YOUR CSV FILE NAME
df = pd.read_csv("retail_sales_eda_dataset.csv")

print("=" * 60)
print("DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nFirst 5 rows:")
print(df.head())


# ------------------------------------------------------------
# 3. DATASET SHAPE
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET SHAPE")
print("=" * 60)

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])


# ------------------------------------------------------------
# 4. COLUMN NAMES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("COLUMN NAMES")
print("=" * 60)

print(df.columns.tolist())


# ------------------------------------------------------------
# 5. DATA TYPES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes)


# ------------------------------------------------------------
# 6. DATASET INFORMATION
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print("=" * 60)

df.info()


# ------------------------------------------------------------
# 7. MISSING VALUES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("MISSING VALUES")
print("=" * 60)

missing_values = df.isnull().sum()

print(missing_values)

print("\nMissing percentage:")
missing_percentage = (df.isnull().sum() / len(df)) * 100
print(missing_percentage.round(2))


# ------------------------------------------------------------
# 8. DUPLICATE VALUES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DUPLICATE RECORDS")
print("=" * 60)

duplicates = df.duplicated().sum()

print("Number of duplicate rows:", duplicates)


# ------------------------------------------------------------
# 9. UNIQUE VALUES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("UNIQUE VALUES")
print("=" * 60)

for column in df.columns:
    print(f"{column}: {df[column].nunique()} unique values")


# ------------------------------------------------------------
# 10. SUMMARY STATISTICS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("SUMMARY STATISTICS")
print("=" * 60)

summary = df.describe(include="all").T

print(summary)


# ------------------------------------------------------------
# 11. CREATE DETAILED SUMMARY TABLE
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("DETAILED SUMMARY TABLE")
print("=" * 60)

numeric_columns = df.select_dtypes(include=np.number).columns

summary_table = df[numeric_columns].describe().T

summary_table["missing"] = df[numeric_columns].isnull().sum()

summary_table["unique"] = df[numeric_columns].nunique()

print(summary_table)


# ------------------------------------------------------------
# 12. IDENTIFY NUMERICAL COLUMNS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("NUMERICAL COLUMNS")
print("=" * 60)

print(numeric_columns.tolist())


# ------------------------------------------------------------
# 13. IDENTIFY CATEGORICAL COLUMNS
# ------------------------------------------------------------

categorical_columns = df.select_dtypes(
    include=["object", "category", "bool"]
).columns

print("\n" + "=" * 60)
print("CATEGORICAL COLUMNS")
print("=" * 60)

print(categorical_columns.tolist())


# ------------------------------------------------------------
# 14. HISTOGRAMS FOR ALL NUMERICAL COLUMNS
# ------------------------------------------------------------

print("\nCreating distributions...")

for column in numeric_columns:

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df[column].dropna(),
        kde=True
    )

    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 15. BOXPLOTS FOR ALL NUMERICAL COLUMNS
# ------------------------------------------------------------

print("\nCreating boxplots...")

for column in numeric_columns:

    plt.figure(figsize=(8, 4))

    sns.boxplot(
        x=df[column].dropna()
    )

    plt.title(f"Boxplot of {column}")
    plt.xlabel(column)

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 16. CORRELATION MATRIX
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CORRELATION MATRIX")
print("=" * 60)

correlation_matrix = df[numeric_columns].corr()

print(correlation_matrix)


# ------------------------------------------------------------
# 17. CORRELATION HEATMAP
# ------------------------------------------------------------

if len(numeric_columns) >= 2:

    plt.figure(figsize=(12, 8))

    sns.heatmap(
        correlation_matrix,
        annot=True,
        cmap="coolwarm",
        fmt=".2f",
        linewidths=0.5
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 18. CATEGORICAL COLUMN ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("CATEGORICAL COLUMN ANALYSIS")
print("=" * 60)

for column in categorical_columns:

    print("\n" + "-" * 50)
    print("Column:", column)

    print(df[column].value_counts().head(10))


# ------------------------------------------------------------
# 19. BAR CHARTS FOR CATEGORICAL COLUMNS
# ------------------------------------------------------------

for column in categorical_columns:

    # Avoid creating charts for columns with too many categories
    if df[column].nunique() <= 15:

        plt.figure(figsize=(8, 5))

        sns.countplot(
            data=df,
            x=column,
            order=df[column].value_counts().index
        )

        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")

        plt.xticks(rotation=45)

        plt.tight_layout()
        plt.show()


# ------------------------------------------------------------
# 20. OUTLIER DETECTION USING IQR
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("OUTLIER ANALYSIS")
print("=" * 60)

outlier_summary = {}

for column in numeric_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    outlier_summary[column] = len(outliers)

    print(f"\n{column}")
    print("Q1:", Q1)
    print("Q3:", Q3)
    print("IQR:", IQR)
    print("Lower limit:", lower_limit)
    print("Upper limit:", upper_limit)
    print("Number of outliers:", len(outliers))


# ------------------------------------------------------------
# 21. OUTLIER SUMMARY TABLE
# ------------------------------------------------------------

outlier_table = pd.DataFrame(
    list(outlier_summary.items()),
    columns=["Column", "Number_of_Outliers"]
)

print("\n" + "=" * 60)
print("OUTLIER SUMMARY")
print("=" * 60)

print(outlier_table)


# ------------------------------------------------------------
# 22. SKEWNESS ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("SKEWNESS ANALYSIS")
print("=" * 60)

skewness = df[numeric_columns].skew()

print(skewness)


# ------------------------------------------------------------
# 23. MEAN, MEDIAN AND STANDARD DEVIATION
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("MEAN / MEDIAN / STANDARD DEVIATION")
print("=" * 60)

statistics_table = pd.DataFrame({
    "Mean": df[numeric_columns].mean(),
    "Median": df[numeric_columns].median(),
    "Standard Deviation": df[numeric_columns].std(),
    "Minimum": df[numeric_columns].min(),
    "Maximum": df[numeric_columns].max()
})

print(statistics_table)


# ------------------------------------------------------------
# 24. FIND STRONG CORRELATIONS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("STRONG CORRELATIONS")
print("=" * 60)

if len(numeric_columns) >= 2:

    corr_pairs = correlation_matrix.unstack()

    corr_pairs = corr_pairs[
        corr_pairs.index.get_level_values(0) !=
        corr_pairs.index.get_level_values(1)
    ]

    corr_pairs = corr_pairs.sort_values(
        key=lambda x: abs(x),
        ascending=False
    )

    print(corr_pairs.head(10))


# ------------------------------------------------------------
# 25. AUTOMATIC BUSINESS INSIGHTS
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

# Insight 1 - Dataset size

print(
    f"\nInsight 1: The dataset contains "
    f"{df.shape[0]} records and {df.shape[1]} columns."
)


# Insight 2 - Missing values

total_missing = df.isnull().sum().sum()

print(
    f"Insight 2: The dataset contains "
    f"{total_missing} missing values in total."
)


# Insight 3 - Duplicate values

print(
    f"Insight 3: The dataset contains "
    f"{duplicates} duplicate records."
)


# Insight 4 - Highest average numerical variable

if len(numeric_columns) > 0:

    means = df[numeric_columns].mean()

    highest_mean_column = means.idxmax()

    print(
        f"Insight 4: Among the numerical variables, "
        f"'{highest_mean_column}' has the highest average value "
        f"of {means[highest_mean_column]:.2f}."
    )


# Insight 5 - Most variable numerical column

if len(numeric_columns) > 0:

    std_values = df[numeric_columns].std()

    highest_variability_column = std_values.idxmax()

    print(
        f"Insight 5: '{highest_variability_column}' "
        f"has the highest standard deviation "
        f"({std_values[highest_variability_column]:.2f}), "
        f"indicating greater variation in its values."
    )


# ------------------------------------------------------------
# 26. TOP VALUES FOR CATEGORICAL VARIABLES
# ------------------------------------------------------------

print("\n" + "=" * 60)
print("TOP CATEGORIES")
print("=" * 60)

for column in categorical_columns:

    if df[column].nunique() <= 20:

        print(f"\n{column}:")

        print(
            df[column]
            .value_counts()
            .head(5)
        )


# ------------------------------------------------------------
# 27. SAVE SUMMARY STATISTICS
# ------------------------------------------------------------

summary_table.to_csv(
    "eda_summary_statistics.csv"
)

outlier_table.to_csv(
    "eda_outlier_summary.csv",
    index=False
)

print("\nSummary files saved successfully.")


# ------------------------------------------------------------
# 28. FINAL EDA REPORT
# ------------------------------------------------------------

print("\n")
print("=" * 60)
print("EDA WORKFLOW COMPLETED")
print("=" * 60)

print("""
The complete Exploratory Data Analysis workflow has been completed.

The analysis included:

1. Dataset loading
2. Dataset shape
3. Column identification
4. Data type analysis
5. Missing-value analysis
6. Duplicate detection
7. Unique-value analysis
8. Summary statistics
9. Numerical-column analysis
10. Categorical-column analysis
11. Distribution visualisation
12. Boxplot analysis
13. Outlier detection
14. Correlation analysis
15. Correlation heatmap
16. Skewness analysis
17. Business insights
18. Summary-statistics export
19. Outlier-summary export

EDA REPORT COMPLETED SUCCESSFULLY.
""")