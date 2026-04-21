# filter numbers divisible by 3
# then square them using map
# one nested line

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map (lambda x: x*x, (filter(lambda x: x%3 == 0, numbers))))
print(result)