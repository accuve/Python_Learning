# Filter Titanic Dataset

# Import necessary libraries
import pandas as pd
import numpy as np

# Load public dataset- titanis dataset from url
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

try:

    print("Data loaded successfully from the URL.") 
    print("First 10 rows of the dataset:")
    print(df.head(10))   
except Exception as e:
    print(f"Error loading data: {e}")

# Filter Individual with age grater than 50
filtered_age_above_50 = df[df['Age'] > 50]
print("\nFiltered DataFrame where Age > 50:")
print(filtered_age_above_50.head(10))

# Filter rows where 'Fare' is greater than 100 and Cabint is not null
filtered_fare_above_100 = df[(df['Fare'] > 100) & (df['Cabin'].notnull())]
print("\nFiltered DataFrame where Fare > 100 and Cabin is not null:")
print(filtered_fare_above_100.head(10))