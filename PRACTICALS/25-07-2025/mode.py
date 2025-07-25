import numpy as np
from scipy import stats

arr = np.array([1, 2, 5, 8, 1, 3, 9, 1, 2, 8, 2, 8, 2, 8, 2])

print(f"Mode: {(stats.mode(arr)).mode}")
