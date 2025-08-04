# Learning Focus: Applying Functions to Coloumn Name
# The .apply() method is very versatile fro applying 
# a function (built-in, custom or lambda) to each element or row/column for
# series or DataFrame

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

# Renaming colum to suitable name
df_renamed = df.rename(columns={
    'old_name_col_1': 'Fruit_Name',
    'Value_A': 'Quantity',
    'Value_B': 'Price',
    'Date_Str': 'Date'
})
print(f"\n DataFrame: {df_renamed}")

# Coverting datatypes
df_renamed['Quantity'] = df_renamed['Quantity'].astype(int)
df_renamed['Price'] = df_renamed['Price'].astype(float)
df_renamed['Date'] = pd.to_datetime(df_renamed['Date'])

# Displaying updated DataFrame
print(f"\n Updated DataFrame:\n {df_renamed}")

# Displaying updated datatype
print(f"\n Updated Datatype: \n {df_renamed.dtypes}")

# Removing Duplicates
df_renamed.drop_duplicates(inplace=True)
print(f"\n Updated DataFrame:\n {df_renamed}")

# Apply a lambda function to a coloumn (element-wise)

## Normal Way
# Let's create a Price_USD Column from by multiplying Price by a factor of 1.6
# Creating a copy of the file
df_function = df_renamed.copy()

# Add new column after Price and Name it Price_USD
df_function.insert(3, 'Price_USD', np.nan)
print(f"\n Updated DataFrame:\n {df_function}")

# Fill Value in Price_USD Column as Price * conversion factor
conversion_factor=1.6
df_function['Price_USD']= df_function['Price']* conversion_factor
df_function['Price_USD'] = df_function['Price_USD'].astype(int)
print(f"\n Updated Df:\n {df_function}")

## Lambda function
conversion_rate_nrs= 141.12
df_function.insert(4,'Price_NPR',df_function['Price_USD'].apply(lambda x: x * conversion_rate_nrs))
print(f"\n Updated DataFrame with Price in NPR:\n {df_function}")