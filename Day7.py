# **Task 1:** Using `random` and `math` modules:
# Generate 5 random numbers between 1-100
# Print each number and its square root (rounded to 2 decimal places)
# Print the largest number from the 5
import math
import random

num=[]
for i in range(5):
    num.append(random.randint(1, 100))
    print(f" number: {num[i]} | sqrt: {math.sqrt(num[i]):.2f}")
print(f"largest: {max(num)}")


# **Task 2:** Create `myutils.py` with 3 functions:
# - celsius_to_fahrenheit(c)
# - is_palindrome(word) — returns True/False
# - count_vowels(word) — returns count of vowels
import myutils
word = "Khushi"
myutils.count_vowels(word)
result = myutils.count_vowels(word)
print(f"Vowels in {word}: {result}")      

celsius = 40
myutils.celsius_to_fahrenheit(40)
print(f"{celsius} In faranhite: {myutils.celsius_to_fahrenheit(40)}")

user_word = input("Enter a word to check for palindrome: ")
myutils.is_palindrome("pallindrome")
print(f"Is '{user_word}' a palindrome? {myutils.is_palindrome(user_word)}")
