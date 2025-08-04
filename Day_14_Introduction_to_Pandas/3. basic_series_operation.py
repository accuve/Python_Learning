# --- Learning Focus: Basic Series Operations ---
# Series support many NumPy-like operations, often automatically aligning by index.

import pandas as pd
import numpy as np

print("\n--- Basic Series Operations ---")
# Create a Series with some data
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40, 50])

print(f"Series s1: {s1}")
print(f"Series s2: {s2}")

# Element-wise addition
print(f"\nElement-wise addition of s1 and s2:{s1 + s2}")
# Element-wise subtraction
print(f"Element-wise subtraction of s1 and s2:{s1 - s2}")
# Element-wise multiplication
print(f"Element-wise multiplication of s1 and s2:{s1 * s2}")
# Element-wise division
print(f"Element-wise division of s1 and s2:{s1 / s2}")
# Element-wise exponentiation
print(f"Element-wise exponentiation of s1 and s2:{s1 ** 2}")

# Applying a NumPy function (e.g., square root)
print(f"\nSquare root of s1: {np.sqrt(s1)}")
# Applying a NumPy function (e.g., logarithm)
print(f"Logarithm of s2: {np.log(s2)}")
# Applying a NumPy function (e.g., sine)
print(f"Sine of s1: {np.sin(s1)}")
# Applying a NumPy function (e.g., cosine)
print(f"Cosine of s2: {np.cos(s2)}")

# Applying a custom function using apply
def custom_function(x):
    return x * 2 + 1
print(f"\nApplying custom function to s1: {s1.apply(custom_function)}")

# Using boolean indexing
print(f"\nBoolean indexing on s1 (values > 2): {s1[s1 > 2]}")

# What happens with misaligned indexes? Pandas handles missing values with NaN (Not a Number)
s3 = pd.Series([100, 200, 300])
s4 = pd.Series([1, 2, 3, 4])
print(f"\nSeries s3: {s3}")
print(f"Series s4: {s4}")
print(f"Element-wise addition of s3 and s4 (misaligned indexes): {s3 + s4}")
# This will show NaN for the index 0 in s3 and index 4 in s4
# Note: NaN values can be handled using methods like fillna() or dropna() if needed.

# Example of filling NaN values
s5 = s3 + s4
s5_filled = s5.fillna(0)  # Fill NaN with 0
print(f"\nFilled Series after addition (NaN replaced with 0): {s5_filled}")