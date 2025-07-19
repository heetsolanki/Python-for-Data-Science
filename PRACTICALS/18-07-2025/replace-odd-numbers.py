import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

for i in arr:
    if i % 2 != 0:
        arr[arr == i] = -1

print(arr)