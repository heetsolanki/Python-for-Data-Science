import numpy as np

arr = np.arange(1, 26).reshape(5, 5)
print("Original array:\n", arr)

row_indices = np.array([1, 2, 3]) 
col_indices = np.array([1, 2, 3]) 

central_subarray = arr[np.ix_(row_indices, col_indices)]
print("\nCentral 3x3 subarray:\n", central_subarray)
