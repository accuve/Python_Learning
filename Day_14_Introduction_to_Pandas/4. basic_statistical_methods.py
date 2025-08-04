import pandas as pd
import numpy as np

# --- Learning Focus: Basic Statistical Methods in Pandas ---
print("\n--- Basic Statistical Methods ---")
# Create a DataFrame with some data
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10, 20, 30, 40, 50],
    'C': [100, 200, 300, 400, 500]
    }
df = pd.DataFrame(data)
print(f"DataFrame:\n{df}")
# Basic statistical methods
print(f"\nMean of each column:\n{df.mean()}")
print(f"Sum of each column:\n{df.sum()}")
print(f"Standard deviation of each column:\n{df.std()}")
print(f"Minimum value in each column:\n{df.min()}")
print(f"Maximum value in each column:\n{df.max()}")
print(f"Median of each column:\n{df.median()}")
print(f"Variance of each column:\n{df.var()}")
print(f"Count of non-NA/null entries in each column:\n{df.count()}")
print(f"Quantiles (0.25, 0.5, 0.75) of each column:\n{df.quantile([0.25, 0.5, 0.75])}")

# Correlation and covariance
print(f"\nCorrelation between columns:\n{df.corr()}")
print(f"Covariance between columns:\n{df.cov()}")

# Applying statistical methods to a Series
s = pd.Series([1, 2, 3, 4, 5])
print(f"\nSeries:\n{s}")
print(f"Mean of Series: {s.mean()}")
print(f"Sum of Series: {s.sum()}")
print(f"Standard deviation of Series: {s.std()}")
print(f"Minimum value in Series: {s.min()}")
print(f"Maximum value in Series: {s.max()}")
print(f"Median of Series: {s.median()}")
print(f"Variance of Series: {s.var()}")
print(f"Count of non-NA/null entries in Series: {s.count()}")
print(f"Quantiles (0.25, 0.5, 0.75) of Series:\n{s.quantile([0.25, 0.5, 0.75])}")

# Correlation and covariance for a Series (not applicable, but shown for consistency)
# Note: Series does not have correlation or covariance methods like DataFrame.
print("\nCorrelation and covariance methods are not applicable for a single Series.")
# Note: For a single Series, correlation and covariance are not defined as they require multiple Series.