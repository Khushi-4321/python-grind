import numpy as np

# 1. Create array of 1-10
# 2. Print sum, mean, max, min
# 3. Filter elements greater than 5

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(arr > 5)            # boolean array
print(arr[arr > 5])       # boolean indexing

# arr > 5 returns a boolean array. 
# arr[arr > 5] uses that boolean array to filter, keeps only elements where True.