
# Learning Focue: Dropping Missing Values
# You can drop rows or columns with missing values using the dropna() method.

# Dropping rows with any missing values
# This will remove any row that contains at least one NaN value.
# axis=0 indicates rows, axis=1 would indicate columns.
# how='any' means if any value in the row is NaN, the row will be dropped.
# how='all' means the row will only be dropped if all values are NaN.
# The inplace parameter determines whether to modify the original DataFrame or return a new one.
# If inplace=True, the original DataFrame is modified.
# If inplace=False, a new DataFrame is returned with the rows dropped.
# Note: Using inplace=True will modify the original DataFrame.

# Importing libraries
import pandas as pd
import numpy as np

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

# Creating a copy of the original DataFrame to demonstrate dropping rows
df_dropped_rows = df.copy() # Copying original DataFrame to avoid modifying it

#Drop rows with any missing values
df_dropped_rows.dropna(axis=0, how='any', inplace=True)
print(f"\nDataFrame after Dropping Rows with Any Missing Values:\n {df_dropped_rows}")

# Drop rows only if All values in the row are NaN
# This will remove rows where all values are NaN.
# Creating another copy of the original DataFrame to demonstrate this
df_dropped_all_nan_rows = df.copy() # Copying original DataFrame to avoid modifying it
df_dropped_all_nan_rows.dropna(axis=0, how='all', inplace=True)

# Creating a copy of the original DataFrame to demonstrate dropping columns
df_dropped_columns = df.copy() # Copying original DataFrame to avoid modifying it

# Dropping columns with any missing values
# This will remove any column that contains at least one NaN value.
df_dropped_columns.dropna(axis=1, how='any', inplace=True)
print(f"\nDataFrame after Dropping Columns with Any Missing Values:\n {df_dropped_columns}")

# Dropping columns only if All values in the column are NaN
# This will remove columns where all values are NaN.
df_dropped_all_nan_columns = df.copy() # Copying original DataFrame to avoid modifying it
df_dropped_all_nan_columns.dropna(axis=1, how='all', inplace=True)
print(f"\nDataFrame after Dropping Columns with All Missing Values:\n {df_dropped_all_nan_columns}")