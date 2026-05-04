import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])

# 1. Print first two rows
# 2. Print last two columns
# 3. Print the element 7
# 4. Print middle 2x2 matrix (elements 6,7,10,11)

print(arr[0:2])
print(arr[:, -2:])
print(arr[1][2])
print(arr [1:3, 1:3])