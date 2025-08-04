# --- Learning Focus: Broadcasting ---
# Broadcasting is a powerful mechanism that allows NumPy to perform operations
# on arrays of different shapes. It automatically "stretches" the smaller array
# to match the shape of the larger array, provided certain rules are met.

import numpy as np
print("\n--- Broadcasting Example ---\n")

# Example 1: Scalar to Array
# A scalar (single number) is broadcast across the entire array.
array_scalar=np.array([[1, 2, 3], [4, 5, 6]])
print("Original Array:\n", array_scalar)
scalar_value = 10
result_scalar = array_scalar + scalar_value
print("After Adding Scalar:\n", result_scalar)

# Example 2: 1-D Array to 2-D Array (Row-wise operation)
# When a 1D array is added to a 2D array, it is broadcast across each row,
# provided the 1D array's size matches the number of columns in the 2D array.
array_2d_broadcast=np.array([[10, 20, 30], [40, 50, 60]])
row_vector = np.array([1, 2, 3])
print("\nOriginal 2D Array:\n", array_2d_broadcast)
result_row_broadcast = array_2d_broadcast + row_vector
print(f"\nAfter Adding Row Vector, {result_row_broadcast}")

# Example 3: 1-D Array to 2-D Array (Column-wise operation - requires reshaping)
# To broadcast a 1D array across columns, it often needs to be reshaped
# into a column vector (e.g., (N, 1) shape).

col_vector = np.array([100, 200]).reshape(2,1) # Reshape to a column vector
print(f"\nColumn Vector:\n{col_vector}")
print(f"Original 2D Array + Column Vector:\n {array_2d_broadcast+col_vector}")
# The col_vector [[100], [200]] is conceptually stretched to [[100,100,100], [200,200,200]]
# and then element-wise addition occurs.

# --- Broadcasting Rules (Simplified) ---
# For two arrays to be broadcastable, their dimensions must be compatible, meaning:
# 1. They are equal.
# 2. One of them is 1.
# The comparison starts with the trailing (rightmost) dimensions and works its way left.