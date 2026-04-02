# Write a recursive function that counts the number of vowels in a string.
# count_vowels("hello") → 2

def count_vowels(s):
    if s =="":
        return 0
    if s[0] in "AEIOUaeiou":
        return 1+ count_vowels(s[1:])
    return 0 + count_vowels(s[1:])

s= "Vowelcheck"
print(count_vowels(s))
