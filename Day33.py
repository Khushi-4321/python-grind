# You have a list of numbers:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map and lambda, create a new list where:
# - Even numbers are squared
# - Odd numbers are cubed
Output = list(map(lambda x: x**2 if  x%2 == 0 else x**3, numbers))
print(Output)

# Output: [1, 4, 27, 16, 125, 36, 343, 64, 729, 100]