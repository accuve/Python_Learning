# --- Your Daily Project: Array Statistics and Broadcasting ---
# Create a 5x5 NumPy array with random integers.
# Calculate the mean of each row and the sum of each column.
# Add a 1D array to each row of the 2D array using broadcasting.

print("\n--- Your Daily Project: Array Statistics and Broadcasting ---")
import numpy as np

# 1. Create a 5x5 NumPy array with random integers (e.g., between 1 and 10)
# np.random.randint(low, high, size) generates integers from low (inclusive) to high (exclusive)

my_5x5_array = np.random.randint(1, 11, size=(5, 5))
print("5x5 Array with Random Integers:")
print(my_5x5_array)

# 2. Calculate the mean of each row
mean_of_rows=np.mean(my_5x5_array, axis=1)
print("\nMean of Each Row:")
print(mean_of_rows)

# 3. Calculate the sum of each column
sum_of_columns = np.sum(my_5x5_array, axis=0)
print("\nSum of Each Column:")
print(sum_of_columns)   

#4. Mean of Each Column
mean_of_columns = np.mean(my_5x5_array, axis=0)
print("\nMean of Each Column:")
print(mean_of_columns)

# 5. Add a 1D array to each row of the 2D array using broadcasting
# Create a 1D array with 5 elements (e.g., [1, 2, 3, 4, 5])
add_vector = np.array([0.1,0.2,0.3,0.4,0.5])
print(f"\n1D Array to Add to Each Row: {add_vector}")
broadcasted_array = my_5x5_array + add_vector
print("\nArray After Broadcasting:")
print(broadcasted_array)