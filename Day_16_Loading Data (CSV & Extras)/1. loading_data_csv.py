#---Importing Required Libraries---
import pandas as pd
import numpy as np

#--- Learning Focus: Loading Data from CSV into Pandas DataFrames ---
# This script demonstrates how to load data from CSV into Pandas DataFrames.

#--- Creating CSV Files ---
csv_content = """Name,Age,Salary,city
Alice,30,70000,New York
Bob,25,50000,Los Angeles
Charlie,35,80000,Chicago
David,28,60000,Houston
Eve,22,45000,Phoenix
Frank,40,90000,Philadelphia
Grace,32,75000,San Antonio
Hannah,29,52000,San Diego
Ivy,27,48000,Dallas
Jack,31,62000,San Jose
"""
# Writing the CSV content to a file to specified path
csv_file_path = '/home/creation/Project/Python/Day_16_Loading Data (CSV & Extras)/csv_data.csv'
with open(csv_file_path, 'w') as file:
    file.write(csv_content)

#--- Loading Data from CSV File ---
try:
    # Attempt to load the CSV file into a DataFrame
    df_csv = pd.read_csv(csv_file_path)
    print("Data loaded from CSV file:")
    print(df_csv)

    #Now reading the CSV file again with different parameters
    df_csv_custom = pd.read_csv(csv_file_path)
    print("\nData loaded from CSV file:")
    print(df_csv_custom)
except FileNotFoundError:
    print(f"Error: The file {csv_file_path} does not exist.")




