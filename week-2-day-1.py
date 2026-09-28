# Week 2 - Day 1: Data Visualisation
# Matplotlib + Seaborn

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. Create Sample Dataset
# -----------------------------
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 180, 160, 220, 250],
    "Profit": [30, 40, 55, 45, 70, 85],
    "Customers": [50, 65, 75, 70, 90, 105]
}

df = pd.DataFrame(data)

print(df)

# Apply Seaborn theme
sns.set_theme(style="whitegrid")


# -----------------------------
# 2. Line Chart
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()


# -----------------------------
# 3. Bar Chart
# -----------------------------
plt.figure(figsize=(8, 5))
sns.barplot(x="Month", y="Sales", data=df)
plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()


# -----------------------------
# 4. Scatter Plot
# -----------------------------
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x="Customers",
    y="Sales",
    data=df,
    s=100
)
plt.title("Customers vs Sales")
plt.xlabel("Number of Customers")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()


# -----------------------------
# 5. Histogram
# -----------------------------
plt.figure(figsize=(8, 5))
sns.histplot(df["Sales"], bins=5, kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()


# -----------------------------
# 6. Box Plot
# -----------------------------
plt.figure(figsize=(6, 5))
sns.boxplot(y=df["Sales"])
plt.title("Sales Box Plot")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("box_plot.png")
plt.show()