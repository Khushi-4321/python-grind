import numpy as np

# 1. Create a 3x3 matrix (2D array) with numbers 1-9
# 2. Print its shape
# 3. Print the second row
# 4. Print the sum of each column

arr = np.array([[1,  2, 3], [4, 5, 6], [7, 8, 9]])
print(arr.shape)
print(arr[1])
print(np.sum(arr, axis = 0))
# print(np.sum(arr, axis=1))    # sum of each row