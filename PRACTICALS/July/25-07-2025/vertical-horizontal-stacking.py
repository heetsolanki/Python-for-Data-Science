import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}\n")
print(f"Vertical stacking: \n{np.vstack((arr1, arr2))}\n")
print(f"Horizontal stacking: \n{np.hstack((arr1, arr2))}")