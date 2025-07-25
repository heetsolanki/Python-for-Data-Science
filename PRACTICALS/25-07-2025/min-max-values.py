import numpy as np

arr = np.random.randint(0, 100, size=(10, 10))
min_value = np.min(arr)
max_value = np.max(arr)

print("Array:")
print(arr)
print(f"\nMinimum value: {min_value}")
print(f"Maximum value: {max_value}")
