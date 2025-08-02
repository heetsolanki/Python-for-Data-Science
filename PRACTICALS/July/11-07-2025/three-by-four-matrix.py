import numpy as np

one_d_array = np.arange(10, 22, 1)

two_d_array = one_d_array.reshape(3, 4)

print("Two-dimensional array (3x4):")
print(two_d_array)