# Temperature Series Analysis
print("Temperature Series Analysis")

import pandas as pd
import numpy as np

# 1. Create a list of temperatures
temperatures = [22.5, 23.0, 21.5, 24.0, 22.0, 23.5, 21.0]
print("Temperatures:", temperatures)

# 2. Create list of dates
dates = pd.date_range(start='2025-07-26', periods=len(temperatures), freq='D')
print("Dates:", dates)

# 3. Create a Pandas Series with temperatures and dates
temperature_series = pd.Series(temperatures, index=dates)
print("Temperature Series:")
print(temperature_series)

# 4. Calculate the mean temperature
mean_temperature = temperature_series.mean()
print("Mean Temperature:", mean_temperature)

# 5. Calculate the maximum temperature
max_temperature = temperature_series.max()
hottest_day = temperature_series.idxmax()
print("Hottest Day:", hottest_day)
print("Maximum Temperature:", max_temperature)

# 6. Calculate the minimum temperature
min_temperature = temperature_series.min()
coldest_day = temperature_series.idxmin()
print("Coldest Day:", coldest_day)
print("Minimum Temperature:", min_temperature)

# 7. Calculate the standard deviation of the temperatures
std_temperature = temperature_series.std()
print("Standard Deviation of Temperatures:", std_temperature)

# 9. Accessing temperature on a specific date
specific_date=pd.to_datetime(input("Enter a date (YYYY-MM-DD) to get the temperature: "))
if specific_date in temperature_series.index:
    specific_temp = temperature_series[specific_date]
    print(f"Temperature on {specific_date}: {specific_temp} °C")
else:
    print(f"No temperature data available for {specific_date}.")