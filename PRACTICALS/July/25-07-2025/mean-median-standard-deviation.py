import numpy as np

arr = np.array([[2,5,8], [3, 7, 4]])

print(f"Mean: {np.mean(arr):.2f}")
print(f"Median: {np.median(arr):.2f}")
print(f"Standard Deviation for axis 0: {np.std(arr, axis=0)}")
print(f"Standard Deviation for axis 1: {np.std(arr, axis=1)}")
