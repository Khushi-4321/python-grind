# Day 17 - Recursion Practice
def recursive_sum(num):
    if num == []:
        return 0
    return num[0] + recursive_sum(num[1:])

print(recursive_sum([1, 2, 3, 4, 5]))