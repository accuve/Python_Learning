# Day 17: Data Filtering
# This script demonstrates how to load a dataset from a URL and filter it using pandas.
# Data filtering helps in selecting specific rows or columns based on certain conditions.


# Import necessary libraries
import pandas as pd
import numpy as np

# Load public dataset- titanis dataset from url
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

try:

    print("Data loaded successfully from the URL.") 
    print("First 10 rows of the dataset:")
    print(df.head(10))   
except Exception as e:
    print(f"Error loading data: {e}")

# Conditinal Filtering (Boolean Indexing)
# Filter rows where 'Age' is greater than 30
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame where Age > 30:")
print(filtered_df.head(10))

# Select Rows where Cabin is null
filtered_null_cabin = df[df['Cabin'].isnull()]
print("\nFiltered DataFrame where Cabin is null:")
print(filtered_null_cabin.head(10))

# Combining multiple conditions using local operators
# Filter rows where 'Age' is greater than 30 and 'Fare' is less than 50
filtered_combined = df[(df['Age'] > 30) & (df['Fare'] < 50)]
print("\nFiltered DataFrame where Age > 30 and Fare < 50:")
print(filtered_combined.head(10))

# Selecting specific columns after filtering
# Filter rows where 'Age' is greater than 30 and select only 'Name', 'Age', and 'Fare' columns
filtered_columns = df[df['Age'] > 30][['Name', 'Age', 'Fare']]
print("\nFiltered DataFrame with specific columns where Age > 30:")
print(filtered_columns.head(10))

# Filter rows where Age is greater than 30 or Age is less than 5
filtered_age_conditions = df[(df['Age'] > 30) | (df['Age'] < 5)]
print("\nFiltered DataFrame where Age > 30 or Age < 5:")
print(filtered_age_conditions.head(10))

# Using .isin() method to filter rows
# Filter rows where 'Pclass' is either 1 or 3
filtered_pclass = df[df['Pclass'].isin([1, 3])]
print("\nFiltered DataFrame where Pclass is either 1 or 3:")
print(filtered_pclass.head(10))

# Using .loc[] for label-based indexing
# Select rows where 'Age' is greater than 30 and only 'Name' and 'Age' columns
filtered_loc = df.loc[df['Age'] > 30, ['Name', 'Age']]
print("\nFiltered DataFrame using .loc[] where Age > 30:")
print(filtered_loc.head(10))

# The difference between .loc[] and .isin()
# .loc[] is used for label-based indexing, while .isin() is used to filter
# based on whether a column's values are in a specified list.