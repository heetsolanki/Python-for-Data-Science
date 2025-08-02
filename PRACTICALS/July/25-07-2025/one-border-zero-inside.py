import numpy as np

arr = np.zeros((5, 5), dtype=int)
arr[0, :] = 1
arr[-1, :] = 1
arr[:, 0] = 1
arr[:, -1] = 1

print(f"Array with one border and zero inside: \n{arr}")