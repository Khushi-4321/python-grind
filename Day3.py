# Create a dictionary of 5 cities and their populations.
# Print only cities with population above 1 million.
# Print the most populated city.

city = {
    "A": 164864368,
    "B": 563638,
    "C": 136834,
    "D": 4544368,
    "E": 646366
}

for key, value in city.items():
    if value > 1000000:
        print(f"{key}")
maxpop = max(city, key = city.get)
print(f"city with maximum population: {maxpop}")        

# =======TASK 1==========
# Write calculate_grade(marks) that returns 
# average, highest, lowest from a list of marks.

def calculator(numbers):
    return min(numbers), max(numbers), sum(numbers)/len(numbers)

low, high, avg = calculator([7, 9, 5, 8, 4])
print(f"low: {low}, high: {high}, average: {avg}")

# **Task 2 — Error Handling:**
# ```
# Ask user to enter two numbers and divide them.
# Handle: non-number input, division by zero.
# Print result if valid, specific error message if not.
# ```
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = num1/num2
    print(f"Result: {result}")

except ValueError: 
    print("Enter an integer")
except ZeroDivisionError:
    print("Cannot divide by zero")

# **Task 3 — Lambda:**
# ```
# You have this list:
# words = ["banana", "apple", "kiwi", "mango", "strawberry"]
# Sort it by length of word using lambda.
# Print sorted list.

words = ["banana", "apple", "kiwi", "mango", "strawberry"]
x = sorted(words, key = lambda x: len(x),  reverse= True)
print(f"result= {x}")
