# Learning Focus: Renaming Columns in Pandas DataFrame
# This script demonstrates how to rename columns in a Pandas DataFrame

# --- Importing Pandas and NumPy ---
import pandas as pd
import numpy as np

# creating a sample Data
data = {
    'old_name_col_1': ['Apple', 'Banana', 'Apple', 'Orange', 'Banana', 'Grape'],
    'Value_A': ['100', '200', '100', '300', '200', '150'], # Stored as string, needs conversion
    'Value_B': [10.5, 20.0, 10.5, 30.0, 20.0, 15.0],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Berry'],
    'Date_Str': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03', '2023-01-02', '2023-01-04']
}

# Creating a DataFrame
df = pd.DataFrame(data)
print("--- Original DataFrame ---")

# Listing all columns before renaming
print(df.columns.tolist())

# Renaming columns
# Using .rename() method to rename columns
# Pass a dictionary with old names as keys and new names as values
# be careful with the column names to ensure they match exactly
# be careful with order of columns to avoid confusion, orelse it can lead to errors
print(df.columns.tolist())
df.rename(columns={
    'old_name_col_1': 'Fruit_Name',
    'Value_A': 'Quantity',
    'Value_B': 'Price',
    'Date_Str': 'Date'
}, inplace=True)
print("--- DataFrame After Renaming Columns ---")
print(df.columns.tolist())

# Displaying the updated DataFrame
print(df)
print("--- Updated DataFrame ---")