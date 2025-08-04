# --- Learning Focus: Accessing Series Elements ---
# You can access elements by their position (integer index) or by their label (custom index).

import numpy as np
import pandas as pd

# Create a Series with a custom index
data_list=[10, 20, 30, 40, 50]
custom_index=['a', 'b', 'c', 'd', 'e']
custom_series = pd.Series(data_list, index=custom_index,name='Custom Series')
print(f"Custom Series with custom index:\n{custom_series}") 

# Accessing elements by position
print("\nAccessing elements by position:")
print(f"Element at position 0: {custom_series[0]}")
print(f"Element at position 2: {custom_series[2]}")

# Accessing elements by label
print("\nAccessing elements by label:")
print(f"Element with label 'a': {custom_series['a']}")
print(f"Element with label 'c': {custom_series['c']}")

# Accessing a range of elements by position
print("\nAccessing a range of elements by position:")
print(f"Elements from position 1 to 3:\n{custom_series[1:4]}")

# Accessing a range of elements by label
print("\nAccessing a range of elements by label:")
print(f"Elements with labels from 'b' to 'd':\n{custom_series['b':'d']}")

# Accessing elements with negative indexing
print("\nAccessing elements with negative indexing:")
print(f"Element at position -1 (last element): {custom_series[-1]}")
print(f"Element at position -3 (third last element): {custom_series[-3]}")
print(f"Elements from position -4 to -2:\n{custom_series[-4:-2]}")

# Accessing elements with a condition
print("\nAccessing elements with a condition:")
condition = custom_series > 20
print(f"Elements greater than 20:\n{custom_series[condition]}")