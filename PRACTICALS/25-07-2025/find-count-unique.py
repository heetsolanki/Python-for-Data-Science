import numpy as np

data = np.array([1, 2, 2, 3, 1, 4, 5, 3, 2, 1])

uniqueElements, counts = np.unique(data, return_counts=True)
print(f"Unique elements: {uniqueElements}\n")

print(f"Count of each unique element:")
for element, count in zip(uniqueElements, counts):
    print(f"Element {element}: {count} times")
