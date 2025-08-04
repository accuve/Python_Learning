# Learning Focus: Converting Data Types in Pandas DataFrame
# This script demonstrates how to convert data types of columns in a Pandas DataFrame

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

# Rename Value_A to Quantity and Value_B to Price for clarity
df.rename(columns={
    'old_name_col_1': 'Fruit_Name',
    'Value_A': 'Quantity',
    'Value_B': 'Price',
    'Date_Str': 'Date'
}, inplace=True)

# Displaying datatypes for all columns before conversion
print("Initial Data Types:\n", df.dtypes)

# Converting 'Quantity' from string to integer
df['Quantity'] = df['Quantity'].astype(int)

# Converting 'Price' from float to integer
df['Price'] = df['Price'].astype(int)

# Converting 'Date' from string to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Displaying datatypes after conversion
print("\nData Types After Conversion:\n", df.dtypes)
# Displaying the updated DataFrame
print("\n--- Updated DataFrame ---")
print(df)