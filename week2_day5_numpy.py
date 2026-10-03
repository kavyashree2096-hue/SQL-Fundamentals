"""
Week 2 - Day 5: NumPy for Data Analysis
Sunrise Healthcare Client Project
"""

import numpy as np
import pandas as pd
import time

# 1. 1D, 2D and 3D arrays
arr_1d = np.array([10, 20, 30, 40, 50])
arr_2d = np.array([[10, 20, 30], [40, 50, 60]])
arr_3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print("1D:\n", arr_1d)
print("2D:\n", arr_2d)
print("3D:\n", arr_3d)

# 2. Vectorised operations
print("Add 10:", arr_1d + 10)
print("Multiply by 2:", arr_1d * 2)
print("Mean:", np.mean(arr_1d))
print("Sum:", np.sum(arr_1d))
print("Std:", np.std(arr_1d))
print("Percentile 75:", np.percentile(arr_1d, 75))

# 3. Boolean masking and fancy indexing
print("Values > 25:", arr_1d[arr_1d > 25])
print("Selected indexes [0,2,4]:", arr_1d[[0, 2, 4]])

# 4. Broadcasting example
a = np.array([[10, 20, 30], [40, 50, 60]])
b = np.array([1, 2, 3])
print("Broadcasting:\n", a + b)

# 5. Compare NumPy vectorisation with Python loops
large = np.arange(1_000_000)

start = time.perf_counter()
loop_result = [x * 2 for x in large]
loop_time = time.perf_counter() - start

start = time.perf_counter()
numpy_result = large * 2
numpy_time = time.perf_counter() - start

print(f"Python loop time: {loop_time:.6f} seconds")
print(f"NumPy vectorised time: {numpy_time:.6f} seconds")
print("NumPy result matches:", np.array_equal(np.array(loop_result), numpy_result))

# 6. Optional: apply NumPy to the Sunrise appointment dataset
path = "data/cleaned_appointments.csv"
try:
    df = pd.read_csv(path)
    numeric = df.select_dtypes(include=np.number)
    if not numeric.empty:
        values = numeric.to_numpy()
        print("\nHealthcare numeric matrix shape:", values.shape)
        print("Column means:", np.nanmean(values, axis=0))
        print("Column std:", np.nanstd(values, axis=0))
        print("Column 25th percentiles:", np.nanpercentile(values, 25, axis=0))
        print("Column 75th percentiles:", np.nanpercentile(values, 75, axis=0))
except FileNotFoundError:
    print(f"\n{path} not found. Run week2_day4_data_cleaning.py first.")
