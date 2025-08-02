import numpy as np

checkboard = np.zeros((5, 5), dtype=int)

checkboard[1::2, ::2] = 1
checkboard[::2, 1::2] = 1

print(f"Checkboard Pattern: \n{checkboard}")