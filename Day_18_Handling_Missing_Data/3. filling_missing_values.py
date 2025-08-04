# Learning Focus: Filling Missing Values in Pandas DataFrame
# This script demonstrates how to fill missing values in a pandas DataFrame.
# It uses pandas' built-in functions to fill NaN values with specified values or methods.

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

# Filling missing values
# Using fillna() to fill NaN values with a specified value

# Fill with a specific value 0 for all missing values
df_filled_zero = df.fillna(0)
print(f"\nDataFrame after Filling Missing Values with 0:\n {df_filled_zero}")

# Fill with the missing value with mean of the column
df_filled_mean = df.copy()
df_filled_mean['Age'] = df_filled_mean['Age'].fillna(df_filled_mean['Age'].mean(),inplace=True)
df_filled_mean['City'] = df_filled_mean['City'].fillna('Kathmandu', inplace=True) # Filling missing city with a default value
df_filled_mean['Salary'] = df_filled_mean['Salary'].fillna(df_filled_mean['Salary'].mean(), inplace=True)
df_filled_mean['Experience'] = df_filled_mean['Experience'].fillna(df_filled_mean['Experience'].mean(), inplace=True)

print(f"\nDataFrame after Filling Missing Values with Mean:\n {df_filled_mean}")

# same can be done using median or mode

# Forward Fill
# Using method='ffill' to propagate the last valid observation forward
df_filled_ffill = df.fillna(method='ffill')
print(f"\nDataFrame after Forward Fill:\n {df_filled_ffill}")

# Backward Fill
# Using method='bfill' to propagate the next valid observation backward
df_filled_bfill = df.fillna(method='bfill')
print(f"\nDataFrame after Backward Fill:\n {df_filled_bfill}")