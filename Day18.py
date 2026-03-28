# Day 18 - Recursion: Count elements in a list
def recursive_count(num):
    if num == []:
        return 0
    return 1 + recursive_count(num[1:])

print(recursive_count([1, 2, 3, 4, 5]))