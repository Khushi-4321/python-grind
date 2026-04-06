# Problem: Write a recursive function that checks if a string contains only digits.
# is_all_digits("12345") → True
# is_all_digits("123a5") → False

def is_all_digits(s):
    if len(s) == 0:
        return True
    if s[0].isdigit() == False:
        return False 
    return is_all_digits(s[1:])

print(is_all_digits("64246"))
print(is_all_digits("65tw4a6"))
    