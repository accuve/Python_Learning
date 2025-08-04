#---Importing required Libraries---
import pandas as pd
import numpy as np

#--- Learning Focus: Loading Data from Excel Files into Pandas DataFrames ---
# This script demonstrates how to load data from Excel files into Pandas DataFrames.


#--- Creating a DataFrame from a dictionary ---
data = {
    'Name': ['Alice', 'Bob', 'Charlie','David', 'Eve'],
    'Age': [24, 27, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Net Worth': [50000, 60000, 70000, 80000, 90000]
}

#--- Creating a DataFrame
df = pd.DataFrame(data)
#--- Saving the DataFrame to an Excel file ---
specified_file_path = '/home/creation/Project/Python/Day_16_Loading Data (CSV & Extras)/excel_data.xlsx'
df.to_excel(specified_file_path)
print(f"DataFrame saved to {specified_file_path}")

#--- Loading Data from Excel File ---
try:
    # Attempt to load the Excel file into a DataFrame
    df_excel = pd.read_excel(specified_file_path)
    print("Data loaded from Excel file:")
    print(df_excel)
except FileNotFoundError:
    print(f"Error: The file {specified_file_path} does not exist.")