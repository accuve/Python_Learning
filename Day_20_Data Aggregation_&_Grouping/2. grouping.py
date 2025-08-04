# --- Importing Pandas ---
import pandas as pd
import numpy as np

# --- Setup: Create a DataFrame for demonstration ---
# We'll create a sample sales data set to practice grouping
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

# Grouping by Single Column
# Group by 'Product' and calculate total sales and units sold
sales_by_product = df.groupby('Product').agg({'Sales': 'sum', 'UnitsSold': 'sum'})
print("\n--- Sales and Units Sold by Product ---")
print(sales_by_product)

# Group by Region and calculate average sales
average_sales_by_region = df.groupby('Region')['Sales'].mean()
print("\n--- Average Sales by Region ---")
print(average_sales_by_region)

# Grouping by Multiple Columns
# Group by 'Category' and 'Region' and calculate total sales
sales_by_category_region = df.groupby(['Category', 'Region']).agg({'Sales': 'sum', 'UnitsSold': 'sum'})
print("\n--- Total Sales and Units Sold by Category and Region ---")
print(sales_by_category_region)


