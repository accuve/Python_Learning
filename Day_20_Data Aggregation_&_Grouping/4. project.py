# --- Your Daily Project: Sales Analysis ---
# Using the original 'df' DataFrame:
# 1. Group the data by 'Category' and find the total sales and total units sold for each category.
# 2. Group the data by 'Region' and find the average sales and max units sold per region.
# 3. Use `.agg()` to group by 'Product' and calculate the 'mean' of 'Sales' and the 'sum' of 'UnitsSold'.

# --- Importing Pandas ---
import pandas as pd
import numpy as np

# --- Setup: Create a DataFrame for demonstration ---
# We'll create a sample sales data set to practice grouping and aggregation.
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


print("\n--- Your Daily Project : Sales Analysis ---")

# 1. Group by 'Category' and find total sales and total units sold for each category.
category_grouped = df.groupby('Category').agg(
    TotalSales=('Sales', 'sum'),
    TotalUnitsSold=('UnitsSold', 'sum')
)

# 2. Group by 'Region' and find average sales and max units sold per region.
region_grouped = df.groupby('Region').agg(
    AverageSales=('Sales', 'mean'),
    MaxUnitsSold=('UnitsSold', 'max')
)

# 3. Group by 'Product' and calculate the mean of 'Sales' and the sum of 'UnitsSold'.
product_grouped = df.groupby('Product').agg(
    MeanSales=('Sales', 'mean'),
    TotalUnitsSold=('UnitsSold', 'sum')
)

print("\n--- Total Sales and Units Sold by Category ---")
print(category_grouped)

