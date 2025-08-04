# --- Load and Inspeact a Punlic Dataset ---
# Load a public dataset from a URL and inspect its contents

import pandas as pd
import numpy as np

# Load the dataset from a URL
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_data = pd.read_csv(url)

# Save the dataset to a local CSV file
file_path = '/home/creation/Project/Python/Day_16_Loading Data (CSV & Extras)/titanic_data.csv'
titanic_data.to_csv(file_path, index=False)

try:
    # Load the dataset from the local CSV file
    titanic_data = pd.read_csv(file_path)
    
    # Perform basic inspection of the dataset
    print("Dataset loaded successfully.")
    #.head method to view the first few rows
    print("First 10 rows of the dataset:")
    print(titanic_data.head(10))
    # Display the database information
    print("\nDataset information:")
    titanic_data.info()
    
    # Display basic statistics of the dataset
    print("\nBasic statistics of the dataset:")
    print(titanic_data.describe())
    
    # Check for missing values in the dataset
    print("\nMissing values in the dataset:")
    print(titanic_data.isnull().sum())

except FileNotFoundError:
    print(f"Error: The file {file_path} was not found. Please check the path and try again.")
except pd.errors.EmptyDataError:
    print("Error: The file is empty. Please check the file content.")
except pd.errors.ParserError:
    print("Error: There was a parsing error while reading the file. Please check the file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("Dataset loaded and inspected successfully.")