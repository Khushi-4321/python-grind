# Flatten this 2D list into a single list:
# pythonmatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]

pythonmatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
newlist = [item for row in pythonmatrix for item in row]
print(newlist)