# --- Your Daily Project: Data Refinement ---
# Clean your dataset:
# 1. Rename the column 'Value_B' to 'Amount'.
# 2. Convert the 'Value_A' column (which is currently string) to a numeric type (integer).
# 3. Remove any duplicate rows based on all columns.
# 4. Create a new column 'Discounted_Amount' by applying a 10% discount to the 'Amount' column.

print("\n--- Your Daily Project: Data Refinement ---")

from math import nan
import pandas as pd
import numpy as np

# Sample DataFrame Creation
#nan indicates missing values
project_data = {
    'Prouct_Name' : ['Laptop', 'Smartphone', 'Tablet', 'Laptop', 'Smartwatch'],
    'Price' : [1000, 500, 300, 1000, nan],
    'Sold' : [5, 10, 15, 5, 20],
    'Region' : ['North', 'South', 'East', 'West', 'North']
}

df = pd.DataFrame(project_data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Renaming the column 'Price' to 'Original_Price' and 'Sold' to 'Quantity Sold'
df.rename(columns={'Price': 'Original_Price'}, inplace=True)
df.rename(columns={'Sold': 'Quantity Sold'}, inplace=True)

# Replacing NaN values in 'Original_Price' with 0
df['Original_Price'].fillna(0, inplace=True)

# Converting 'Original_Price' and Quantity Sold to numeric type (float)
# Errors='coerce' will convert non-convertible values to NaN
df['Original_Price'] = pd.to_numeric(df['Original_Price'], errors='coerce')
df['Quantity Sold'] = pd.to_numeric(df['Quantity Sold'], errors='coerce')

# Removing duplicate rows based on all columns
df.drop_duplicates(inplace=True)

# Creating a new column 'Discounted_Price' by applying a 10% discount to 'Original_Price'
Discount_Rate = float(0.10)  # 10% discount
df['Discount_Rate'] = Discount_Rate*100
df['Discounted_Price'] = df['Original_Price'] * (1 - Discount_Rate)

# Display the cleaned DataFrame
print("\nCleaned DataFrame:")
print(df)