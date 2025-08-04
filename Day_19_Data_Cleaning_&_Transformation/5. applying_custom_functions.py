# Learning Focus: Applying custom functions to DataFrame


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

# creating dataframe using above dictionaries
df = pd.DataFrame(data)
print(f"\n DataFrame: {df}")

# Applying a custom function
def categorize_value(value):
    if value < 1000:
        return 'Low'
    elif 1000 <= value < 2000:
        return 'Medium'
    else:
        return 'High'

df['Value_Catefory'] = df['Value_A'].astype(int).apply(categorize_value)
print(f"\n DataFrame with Value Category:\n {df}")
