# Write a recursive function that finds the sum of digits of a number.
# sum_of_digits(1234) → 10
# No loops. Input is an integer, not a string.

def sum_of_digits(numb):
    if numb == 0:
        return 0
    return numb % 10 +  sum_of_digits(numb//10)


numb = int(input("Enter a digit: "))

print(sum_of_digits(numb))