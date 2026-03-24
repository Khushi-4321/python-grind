# Takes a list of numbers
# Returns the sum of all elements
# No loops allowed No sum() built-in

def recursive_sum(num):
    if num == []:
        return 0
    return num[0] + recursive_sum(num[1:])

num = [6,9,4,8]
print(recursive_sum(num))


# recursive_max([3, 7, 2, 9, 1]) → 9
def recursive_max(num):
    if num == []:
        return 0
    elif num[0] > recursive_max(num[1:]):
        return num[0]
    else: 
        return recursive_max(num[1:]) 
    
num = [3, 7, 2, 9, 1]    
print(recursive_max(num))
