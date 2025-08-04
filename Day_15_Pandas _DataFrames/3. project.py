# ---Student Info DataFrame---
# Create a pandas DataFrame to store student information
# The DataFrame should include the following columns:
# 'Name', 'Age', 'Grade', 'Major', 'GPA'
# Add a new column for City. Print DataFrame and its shape.

import pandas as pd
import numpy as np

# Create a DataFrame with student information
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [20, 21, 22, 23],
    'Grade': ['A', 'B', 'C', 'B'],
    'Major': ['Math', 'Science', 'History', 'Art'],
    'GPA': [3.5, 3.0, 2.8, 3.2]
}

# Create the DataFrame
students_df = pd.DataFrame(data)

# Add a new column for City
students_df['City'] = ['New York', 'Los Angeles', 'Chicago', 'Houston']

# Print the DataFrame and its shape
print(students_df)
print("Shape of the DataFrame:", students_df.shape)
# Output the DataFrame and its shape
# The DataFrame should now include the new 'City' column and display its shape.
# The output will show the DataFrame with all columns and the shape indicating the number of rows and columns.
# The expected shape is (4, 6) indicating 4 rows and 6 columns
# as we added the 'City' column to the original 5 columns.
