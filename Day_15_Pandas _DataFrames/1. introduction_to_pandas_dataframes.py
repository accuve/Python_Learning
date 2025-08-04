# Data 15 Frames in Pandas
# Introduction to Pandas DataFrames

# Imporing necessary libraries
import pandas as pd
import numpy as np


# --- Learning Focus: What is a Pandas DataFrame? ---
# A DataFrame is a 2-dimensional labeled data structure with columns of potentially
# different types. You can think of it like a spreadsheet, a SQL table, or a
# dictionary of Series objects.
# It is the most commonly used Pandas object.

# --- Learning Focus: Creating Pandas DataFrames ---
# DataFrames can be created from various inputs:

print("--- Creating DataFrame from a Dictionary of Lists ---")
# Each key in the dictionary becomes a column name.
# Each list becomes the data for that column.

data_dict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df1=pd.DataFrame(data_dict)
print(f"DataFrame from dictionary:\n{df1}\n")
print(f"Type of df1: {type(df1)}\n")
print(f"Shape of df1: {df1.shape}\n")  # (rows, columns)
print(f"Columns in df1: {df1.columns.tolist()}\n")
print(f"Data types in df1:\n{df1.dtypes}\n")
print(f"Index:{df1.index.tolist()}\n")

print("--- Creating DataFrame from a List of Dictionaries ---")
# Each dictionary in the list becomes a row in the DataFrame.
data_list = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]
df2 = pd.DataFrame(data_list)
print(f"DataFrame from list of dictionaries:\n{df2}\n")
print(f"Type of df2: {type(df2)}\n")
print(f"Shape of df2: {df2.shape}\n")  # (rows, columns)
print(f"Columns in df2: {df2.columns.tolist()}\n")
print(f"Data types in df2:\n{df2.dtypes}\n")
print(f"Index:{df2.index.tolist()}\n")

# --- Creating DataFrame from a NumPy Array ---
print("--- Creating DataFrame from a NumPy Array ---")
# You can also create a DataFrame from a NumPy array, specifying column names.
data_array = np.array([[1, 'Alice', 25],
                       [2, 'Bob', 30],
                       [3, 'Charlie', 35]])
df3 = pd.DataFrame(data_array, columns=['ID', 'Name', 'Age'])
print(f"DataFrame from NumPy array:\n{df3}\n")
print(f"Type of df3: {type(df3)}\n")
print(f"Shape of df3: {df3.shape}\n")  # (rows, columns)
print(f"Columns in df3: {df3.columns.tolist()}\n")
print(f"Data types in df3:\n{df3.dtypes}\n")
print(f"Index:{df3.index.tolist()}\n")

#Creating Empty DataFrame
print("--- Creating an Empty DataFrame ---")
# You can create an empty DataFrame and then add data later.
empty_df = pd.DataFrame()
print(f"Empty DataFrame:\n{empty_df}\n")
print(f"Type of empty_df: {type(empty_df)}\n")
print(f"Shape of empty_df: {empty_df.shape}\n")  # (rows, columns)
print(f"Columns in empty_df: {empty_df.columns.tolist()}\n")
print(f"Data types in empty_df:\n{empty_df.dtypes}\n")
print(f"Index:{empty_df.index.tolist()}\n")

# --- Summary ---
# In this lesson, we learned how to create Pandas DataFrames from various data structures
# such as dictionaries, lists of dictionaries, and NumPy arrays. We also saw how to
# create an empty DataFrame. DataFrames are powerful tools for data manipulation and analysis
# in Python, providing a flexible and efficient way to work with structured data.
# In the next lesson, we will explore how to manipulate and analyze data within these DataFrames.
# Stay tuned for more on Pandas DataFrames!