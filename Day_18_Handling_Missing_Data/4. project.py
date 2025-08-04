# --- Your Daily Project: Clean Missing Data ---
# Intentionally introduce some missing values (NaN) into a new DataFrame.
# Practice:
# 1. Identify how many missing values are in each column.
# 2. Create a new DataFrame where rows with *any* missing values are dropped.
# 3. Create another new DataFrame where missing 'Age' values are filled with the mean age.
# 4. Create a third new DataFrame where missing 'City' values are filled with a specific string 'Unknown'.


import pandas as pd
import numpy as np

print("\n--- Your Daily Project: Clean Missing Data ---")

# Create a fresh DataFrame for the project with some NaNs
project_data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam', 'Speakers'],
    'Price': [1200, 25, np.nan, 300, 50, np.nan],
    'UnitsSold': [10, 50, 30, np.nan, 20, 15],
    'Region': ['North', 'South', 'East', 'North', 'West', np.nan],
    'Rating': [4.5, 3.8, 4.2, 3.9, np.nan, 4.0]
}

# Create the DataFrame
project_df = pd.DataFrame(project_data)
print(f"\nOriginal DataFrame with Missing Values:\n{project_df}")

# 1. Identify how many missing values are in each column
missing_counts = project_df.isnull().sum()
print(f"\nMissing Values Count in Each Column:\n{missing_counts}")

# 2. Identify total number of missing values in the DataFrame
total_missing = project_df.isnull().sum().sum()
print(f"\nTotal Number of Missing Values in the DataFrame: {total_missing}")

# 3. Identify rows with any missing values and drop them
cleaned_df_any = project_df.dropna()
print(f"\nDataFrame after Dropping Rows with Any Missing Values:\n{cleaned_df_any}")

# 4. Create A new DataFrame with following conditions:
# missing 'Price' values are filled with the mean price
# missing 'UnitsSold' values are filled with the median units sold
# Region with backward fill
# rating with forward fill
cleaned_df_fill = project_df.copy()
cleaned_df_fill['Price'].fillna(cleaned_df_fill['Price'].mean(), inplace=True)
cleaned_df_fill['UnitsSold'].fillna(cleaned_df_fill['UnitsSold'].median(), inplace=True)
cleaned_df_fill['Region'].fillna(method='ffill', inplace=True)
cleaned_df_fill['Rating'].fillna(method='bfill', inplace=True)
print(f"\nDataFrame after Filling Missing Values:\n{cleaned_df_fill}")