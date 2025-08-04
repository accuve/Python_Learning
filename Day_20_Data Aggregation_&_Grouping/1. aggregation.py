# --- Importing Pandas ---
import pandas as pd
import numpy as np

# --- Setup: Create a DataFrame for demonstration ---
# We'll create a sample sales data set to practice aggregation.
sales_data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Monitor', 'Mouse', 'Laptop', 'Keyboard'],
    'Category': ['Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics'],
    'Region': ['North', 'South', 'East', 'North', 'West', 'South', 'East', 'East'],
    'Sales': [1200, 25, 75, 1300, 300, 30, 1150, 80],
    'UnitsSold': [5, 10, 20, 6, 2, 12, 4, 18]
}
df = pd.DataFrame(sales_data)

print("--- Original DataFrame ---")
print(df)

# Basic Aggregation
# Calculate total sales and units sold
total_sales = df['Sales'].sum()
total_units_sold = df['UnitsSold'].sum()
print("\n--- Total Sales and Units Sold ---")
print(f"Total Sales: {total_sales}")
print(f"Total Units Sold: {total_units_sold}")

# Average Sales per Product
average_sales = df.groupby('Product')['Sales'].mean()
print("\n--- Average Sales per Product ---")
print(average_sales)