# --- Learning Focus: Basic DataFrame Attributes ---
# DataFrames have several attributes that provide information about their structure and content.
# An empty DataFrame can be created with no data or columns.

# Importing necessary libraries
import pandas as pd
import numpy as np

# Creating data list and converting to DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data) # Creating a DataFrame from a dictionary

print("--- Basic DataFrame Attributes ---")
print(f"DataFrame:\n{df}\n")
print(f"Type of df: {type(df)}\n")  # Type of the DataFrame
print(f"Shape of df: {df.shape}\n")  # Shape of the DataFrame (rows, columns)
print(f"Columns in df: {df.columns.tolist()}\n")  # List of column names
print(f"Rows in df:" f"{df.index.tolist()}\n")  # List of index labels
print(f"Data types in df:\n{df.dtypes}\n")  # Data types of each column
print(f"Values as a NumPy array:\n{df.values}\n")  # Values in the DataFrame as a NumPy array

# --- Learning Focus: Adding and Modifying DataFrame Attributes ---
# You can add new columns or modify existing ones in a DataFrame.
print("--- Adding and Modifying DataFrame Attributes ---")
# Adding a new column
df['Salary'] = [70000, 80000, 90000]
print(f"DataFrame after adding 'Salary' column:\n{df}\n")

# Modifying an existing column
df['Age'] = df['Age'] + 1  # Incrementing age by 1
print(f"DataFrame after modifying 'Age' column:\n{df}\n")