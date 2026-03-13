# celsius_to_fahrenheit(c)
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

#is_palindrome(word) — returns True/False
def is_palindrome(word):
    if word == word[::-1]: 
        return True
    else:
        return False
    
    
#count_vowels(word) — returns count of vowels        
def count_vowels(word):
    count = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            count = count+1
    return count  
