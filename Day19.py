# Day 19 - Recursion: Find minimum in a list
def recursive_min(num):
    if len(num) == 1:
        return num[0]
    rest = recursive_min(num[1:])
    return num[0] if num[0] < rest else rest

print(recursive_min([3, 7, 1, 9, 2]))