# Learning Focus : Removing Duplicates in Pandas DataFrame
# This script demonstrates how to remove duplicate rows from a Pandas DataFrame

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

# Renaming columns for clarity, Old_name_col_1 to Fruit_Name, Value_A to Quantity, Value_B to Price
df.rename(columns={
    'old_name_col_1': 'Fruit_Name',
    'Value_A': 'Quantity',
    'Value_B': 'Price',
    'Date_Str': 'Date'
}, inplace=True)

# Converting 'Quantity' from string to integer, 'Price' to float, and 'Date_str' from string to datetime
df['Quantity'] = df['Quantity'].astype(int)
df['Price'] = df['Price'].astype(float)
df['Date'] = pd.to_datetime(df['Date'])

# Displaying updated DataFrame
print(f"\n Updated DataFrame:\n {df}")

# Displayig updated datatype
print(f"\n Updated Datatype: \n {df.dtypes}")