def recursive_sum(num):
    if num == []:
        return 0
    return num[0] + recursive_sum(num[1:])

num = [6,9,4,8]
print(recursive_sum(num))