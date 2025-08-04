# Day 17: Data Selection
# This script demonstrates how to select data in a DataFrame using pandas.

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

# Leaning Focus: Data Selection

# Selecting Columns
# Select a single column
print("Selecting a single column 'Name':")
print(df['Name'].head())  # Displaying the first few entries of the 'Name' column

# Select multiple columns
print("\nSelecting multiple columns 'Name' and 'Age':")
age_fare = df[['Name', 'Age']]
print(f"Name and Age columns:\n{age_fare.head()}")

# Selecting Rows
#Pandas provides iloc for row selection
# Select first row by index position
print("\nSelecting the first row using iloc:")
print(df.iloc[0])  # Displaying the first row of the DataFrame

# Select rows from position 0 to 4 not including 5
print("\nSelecting rows from position 0 to 4 using iloc:")
print(df.iloc[0:5])  # Displaying rows from index 0 to 4

# Select specific rows by a list of positions (fancy indexing)
print("\nSelecting specific rows using a list of positions:")
print(df.iloc[[0, 2, 4]])  # Displaying rows at index 0, 2, and 4

# selec specific rows and columns by a list of positions
print("\nSelecting specific rows and columns using a list of positions:")
print(df.iloc[[0, 2, 4], [1, 3]])
# Displaying rows at index 0, 2, and 4 for columns at index 1 and 3

# Selecting Rows Based on Conditions
# Select rows where Age is greater than 30
print("\nSelecting rows where Age is greater than 30:")
print(df[df['Age'] > 30].head())  # Displaying the first few entries where Age is greater than 30

# Select rows where Age is greater than 30 and Fare is less than 50
print("\nSelecting rows where Age is greater than 30 and Fare is less than 50:")
print(df[(df['Age'] > 30) & (df['Fare'] < 50)].head())  # Displaying the first few entries that meet both conditions

#.loc (label-location based indexing)
# it differs from iloc in that it uses labels instead of integer positions
# difference between loc and iloc is that loc is label based, while iloc is integer position based
# index based indexing means that you can select rows and columns by their labels, while position based indexing means you can select rows and columns by their integer positions
# integer positions are the default index of a DataFrame, while labels are the index that you can set yourself
# Select rows by label
print("\nSelecting rows by label using loc:")
print(df.loc[0])  # Displaying the row with label 0

# Select rows by label range
print("\nSelecting rows by label range using loc:")
print(df.loc[0:4])  # Displaying rows with labels from 0 to 4
# Select specific rows and columns by label
print("\nSelecting specific rows and columns by label using loc:")
print(df.loc[[0, 2, 4], ['Name', 'Age']])
# Displaying rows with labels 0, 2, and 4 for columns 'Name' and 'Age'
# Select rows where 'Age' is greater than 30 using loc
print("\nSelecting rows where 'Age' is greater than 30 using loc:")
print(df.loc[df['Age'] > 30].head())  # Displaying the first few entries where Age is greater than 30

# Resetting the index
# Resetting the index of the DataFrame
# What this does is it creates a new index for the DataFrame, starting from 0
print("\nResetting the index of the DataFrame:")
df_reset = df.reset_index(drop=True)  # drop=True means we don't want to keep the old index as a column
print(df_reset.head())  # Displaying the first few rows

