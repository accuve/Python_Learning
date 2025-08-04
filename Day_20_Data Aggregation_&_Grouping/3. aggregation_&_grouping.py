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

# Multiple Aggregations
# Group by 'Product' and calculate total sales and average units sold
agg_sales = df.groupby('Product').agg(
    TotalSales=('Sales', 'sum'),
    AverageUnitsSold=('UnitsSold', 'mean')
)
print("\n--- Aggregated Sales Data ---")
print(agg_sales)

# Applying a list of funtions to multiple columns
agg_multiple = df.groupby('Product').agg(
    TotalSales=('Sales', 'sum'),
    AverageUnitsSold=('UnitsSold', 'mean'),
    MaxSales=('Sales', 'max'),
    MinUnitsSold=('UnitsSold', 'min')
)
print("\n--- Multiple Aggregations on Sales Data ---")
print(agg_multiple)

#You can reset the index if needed
agg_multiple_reset = agg_multiple.reset_index()
print("\n--- Aggregated Data with Reset Index ---")
print(agg_multiple_reset)