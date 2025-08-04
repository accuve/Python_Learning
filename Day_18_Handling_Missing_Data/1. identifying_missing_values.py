# Day 18: Handling Missing Data
# This script demonstrates how to identify missing values in a pandas DataFrame.
# It uses pandas' built-in functions to check for NaN values and count them.

# Importing libraries
import pandas as pd
import numpy as np

# Setup: Create a DataFrame with intentional missing values
# This DataFrame simulates a dataset with some missing entries.
# In a real-world scenario, you would load your data from a file or database.
# Here, we create a sample DataFrame with some NaN values to demonstrate handling missing data
# using pandas.
data_with_missing = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Age': [30, 24, np.nan, 35, 29, 42, np.nan], # Missing ages for Charlie and Grace
    'City': ['New York', 'London', 'Paris', 'Tokyo', np.nan, 'London', 'Berlin'], # Missing city for Eve
    'Salary': [70000, np.nan, 85000, 60000, 92000, 55000, 78000], # Missing salary for Bob
    'Experience': [5, 2, 10, 7, 15, np.nan, 3] # Missing experience for Frank
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data_with_missing)

# Display the original DataFrame
print(f"Original DataFrame with Missing Values:\n {df}")

# Identifying missing values
# Using isnull() to identify missing values in the DataFrame
missing_values = df.isnull()
print(f"\nMissing Values in DataFrame:\n {missing_values}")

# .notnull() can be used to find non-missing values
non_missing_values = df.notnull()
print(f"\nNon-Missing Values in DataFrame:\n {non_missing_values}")

# .notna() is an alias for .notnull()
# It can also be used to find non-missing values
non_missing_values_alias = df.notna()
print(f"\nNon-Missing Values using .notna():\n {non_missing_values_alias}")

#.sum() can be used to count the number of missing values in each column
missing_count = df.isnull().sum()
print(f"\nCount of Missing Values in Each Column:\n {missing_count}")

# Total missing values in the DataFrame
total_missing = df.isnull().sum().sum()
print(f"\nTotal Missing Values in DataFrame: {total_missing}")