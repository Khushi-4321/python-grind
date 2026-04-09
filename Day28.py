# Write a dict comprehension that creates a dictionary of words and their lengths.
# pythonwords = ["cat", "elephant", "dog", "tiger", "python"]
# # Expected: {'cat': 3, 'elephant': 8, 'dog': 3, 'tiger': 5, 'python': 6}


pythonwords = ["cat", "elephant", "dog", "tiger", "python"]
words = {i: len(i) for i in pythonwords}

print(words)