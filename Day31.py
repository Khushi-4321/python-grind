# Given a list of numbers, return squares of only the even numbers.

# Input:  [1, 2, 3, 4, 5, 6]
# Expected Output: [4, 16, 36]

# Rules:
# - Use filter to get even numbers
# - Use map to square them
# - Use lambda inside both
# - No list comprehension
# - Two steps allowed — filter first, then map

numbers = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x%2 == 0, numbers))
square = list(map(lambda x: x * x, even))

print(square)
