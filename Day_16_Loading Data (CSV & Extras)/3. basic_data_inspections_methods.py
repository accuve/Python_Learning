# --- Learning Focus: Basic Data Inspection Methods ---
# Once data is loaded, we can use various methods to inspect its
# structure, types, and contents. This is crucial for understanding the data
# before performing any analysis or transformations.

# Importing necessary libraries
import pandas as pd
import numpy as np

# Importing csv file
file_path = '/home/creation/Project/Python/Day_16_Loading Data (CSV & Extras)/csv_data.csv'
data = pd.read_csv(file_path)
print("\nData loaded from successfully.")
print(data)

# .head() method
# Displays the first few rows of the DataFrame
print("\nFirst 5 rows of the DataFrame:")
print(data.head())
# default is 5 rows, but you can specify a different number
print("\nFirst 3 rows of the DataFrame:")
print(data.head(3))

# .tail() method
# Displays the last few rows of the DataFrame
print("\nLast 5 rows of the DataFrame:")
print(data.tail())
# default is 5 rows, but you can specify a different number
print("\nLast 3 rows of the DataFrame:")
print(data.tail(3))

# .info() method
# Provides a concise summary of the DataFrame, including the number of non-null entries,
# data types, and memory usage
print("\nDataFrame info:")
data.info()

# .describe() method
# Generates descriptive statistics for numerical columns
print("\nDescriptive statistics of numerical columns:")
print(data.describe())

# .shape attribute
# Returns a tuple representing the dimensions of the DataFrame (rows, columns)
print("\nShape of the DataFrame (rows, columns):")
print(data.shape)

# .columns attribute
# Returns the column labels of the DataFrame
print("\nColumn labels of the DataFrame:")
print(data.columns)

# .dtypes attribute
# Returns the data types of each column in the DataFrame
print("\nData types of each column:")
print(data.dtypes)

# .isnull() method
# Checks for missing values in the DataFrame
print("\nChecking for missing values in the DataFrame:")
print(data.isnull().sum())

# .nunique() method
# Returns the number of unique values in each column
print("\nNumber of unique values in each column:")
print(data.nunique())

# .index attribute
# Returns the index (row labels) of the DataFrame
print("\nIndex (row labels) of the DataFrame:")
print(data.index)

# .sample() method
# Returns a random sample of rows from the DataFrame
print("\nRandom sample of 3 rows from the DataFrame:")
print(data.sample(3))   

# .memory_usage() method
# Returns the memory usage of each column in the DataFrame
print("\nMemory usage of each column:")
print(data.memory_usage())

# .value_counts() method
# Returns the counts of unique values in a specified column
print("\nValue counts for the 'Category' column:")
if 'Category' in data.columns:
    print(data['Category'].value_counts())
else:
    print("Column 'Category' does not exist in the DataFrame.")