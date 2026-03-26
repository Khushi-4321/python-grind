# Write a recursive function that reverses a list.
# recursive_reverse([1, 2, 3, 4, 5]) → [5, 4, 3, 2, 1]

def recursive_reverse(num):
    if num == []:
        return []
    return [num[-1]]+ recursive_reverse(num[:-1])

num = [1, 2, 3, 4, 5]
print(f"{recursive_reverse(num)}")