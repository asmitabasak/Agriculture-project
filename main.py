import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. LOAD DATASET
# -----------------------------
df = pd.read_csv("data/agriculture_data.csv")

print("Dataset Shape:", df.shape)
print("\nDataset Information:")
print(df.info())

print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# 2. DATA CLEANING
# -----------------------------

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Fill numerical missing values with median
numeric_columns = df.select_dtypes(include=np.number).columns

for column in numeric_columns:
    df[column] = df[column].fillna(df[column].median())

# Fill categorical missing values with mode
categorical_columns = df.select_dtypes(include="object").columns

for column in categorical_columns:
    df[column] = df[column].fillna(df[column].mode()[0])

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nCleaned Dataset Shape:", df.shape)

# -----------------------------
# 3. SEASONAL ANALYSIS
# -----------------------------

seasonal_production = (
    df.groupby("Season")["Production"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAverage Production by Season:")
print(seasonal_production)

# -----------------------------
# 4. SEASONAL PRODUCTION GRAPH
# -----------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    x=seasonal_production.index,
    y=seasonal_production.values
)

plt.title("Average Agricultural Production by Season")
plt.xlabel("Season")
plt.ylabel("Average Production")
plt.tight_layout()

plt.savefig("outputs/seasonal_production.png")
plt.show()

# -----------------------------
# 5. CROP-WISE ANALYSIS
# -----------------------------

crop_production = (
    df.groupby(["Season", "Crop"])["Production"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(10, 6))

sns.barplot(
    data=crop_production,
    x="Season",
    y="Production",
    hue="Crop"
)

plt.title("Crop Production Across Seasons")
plt.xlabel("Season")
plt.ylabel("Average Production")
plt.tight_layout()

plt.savefig("outputs/crop_comparison.png")
plt.show()

# -----------------------------
# 6. CORRELATION ANALYSIS
# -----------------------------

numeric_df = df.select_dtypes(include=np.number)

correlation = numeric_df.corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Agricultural Parameter Correlation")
plt.tight_layout()

plt.savefig("outputs/correlation_heatmap.png")
plt.show()

# -----------------------------
# 7. RESOURCE ANALYSIS
# -----------------------------

resource_columns = [
    column for column in
    ["Water_Usage", "Fertilizer_Usage"]
    if column in df.columns
]

if resource_columns:
    resource_analysis = df[
        resource_columns + ["Production"]
    ].corr()

    print("\nResource vs Production:")
    print(resource_analysis)

# -----------------------------
# 8. FINAL SUMMARY
# -----------------------------

print("\n========== PROJECT SUMMARY ==========")

highest_season = seasonal_production.idxmax()
lowest_season = seasonal_production.idxmin()

print("Highest average production season:", highest_season)
print("Lowest average production season:", lowest_season)

print("\nAnalysis completed successfully!")