#Day 14: Introduction to Pandas - Series

# --- Importing Pandas ---
# It's standard practice to import Pandas with the alias 'pd'.
# If you used Anaconda, Pandas is likely already installed.
# If not, open your terminal or command prompt and type:
# pip install pandas
import pandas as pd
import numpy as np # Pandas often works closely with NumPy, so we'll import it too

# --- Learning Focus: What is Pandas? ---
# Pandas is an open-source library providing high-performance, easy-to-use
# data structures and data analysis tools for the Python programming language.
# It's built on top of NumPy and provides two primary data structures:
# 1. Series: A one-dimensional labeled array.
# 2. DataFrame: A two-dimensional labeled data structure with columns of potentially
#    different types (like a spreadsheet or SQL table).


# --- Learning Focus: Creating Pandas Series ---
# A Series can be created from various inputs:
print("--- Creating Series from List ---")
# By default, a numeric index (0, 1, 2...) is created.
data_list= [10, 20, 30, 40]
series_from_list = pd.Series(data_list)
print(series_from_list)
print(f"Index of the Series: {series_from_list.index}")
print(f"Values of the Series: {series_from_list.values}")
print(f"Data type of the Series: {series_from_list.dtype}")

print("\n--- Creating Series from List with Custom Index ---")
# You can specify a custom index (labels)
data_list_with_index = [10, 20, 30, 40]
custom_index = ['a', 'b', 'c', 'd']
series_with_custom_index = pd.Series(data_list_with_index, index=custom_index)
print(series_with_custom_index)
print(f"Index of the Series with custom index: {series_with_custom_index.index}")
print(f"Values of the Series with custom index: {series_with_custom_index.values}")
print(f"Data type of the Series with custom index: {series_with_custom_index.dtype}")

print("\n--- Creating Series from NumPy Array ---")
# You can also create a Series from a NumPy array.
numpy_array = np.array([1, 2, 3, 4])
series_from_numpy = pd.Series(numpy_array)
print(numpy_array)
print(series_from_numpy)
print(f"Index of the Series from NumPy: {series_from_numpy.index}")
print(f"Values of the Series from NumPy: {series_from_numpy.values}")
print(f"Data type of the Series from NumPy: {series_from_numpy.dtype}")


print("\n--- Creating Series from Dictionary ---")
# A Series can also be created from a dictionary.
data_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
series_from_dict = pd.Series(data_dict)
print(series_from_dict)
print(f"Index of the Series from Dict: {series_from_dict.index}")
print(f"Values of the Series from Dict: {series_from_dict.values}")
print(f"Data type of the Series from Dict: {series_from_dict.dtype}")

# You can also give a Series a name
print("\n--- Naming a Series ---")
data_list_named = [1, 2, 3]
custom_index = ['x', 'y', 'z']
series_named = pd.Series(data_list_named, index=custom_index, name='MySeries')
print(series_named)
print(f"Name of the Series: {series_named.name}")
print(f"Index of the Named Series: {series_named.index}")
print(f"Values of the Named Series: {series_named.values}")
print(f"Data type of the Named Series: {series_named.dtype}")