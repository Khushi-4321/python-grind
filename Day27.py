# Write a list comprehension that filters only words longer than 4 characters from this list:
# pythonwords = ["cat", "elephant", "dog", "tiger", "ox", "python"]

pythonwords = ["cat", "elephant", "dog", "tiger", "ox", "python"]
words = [i for i in pythonwords if len(i)>4 ]
print(words)