# Use filter and lambda to get odd numbers

numbers = [1, 2, 3, 4, 5]
odd = list(filter(lambda x: x%2!= 0, numbers))
print(odd)