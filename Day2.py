# # **Task 1 — Strings:**
# # ```
# # Take a sentence as input.
# # Print: word count, character count (no spaces), 
# # and the sentence in title case.

# name = input("Enter a sentence: ")
# words = (len(name.split()))
# characters = len(name.replace(" ", ""))
# # words = (len(name))
# print(f"words = {words}" )
# print(f"characters = {characters}")
# print(name.title())

# # **Task 2 — Dictionaries:**
# # ```
# # Create a dictionary of 5 students with name as key and marks as value.
# # Print only students who scored above 75.
# # Print the topper (highest marks).
# # ```

# students = {

#     "A": 56,
#     "B": 97,
#     "C": 59,
#     "D": 79,
#     "E": 84
# }
# for key, value in students.items():
#     if value >75:
#          print(f" {key}, {value}")

# topper = max(students, key = students.get)     
# print(f"topper = {topper}")

# # **Task 3 — List Comprehension:**
# # ```
# # Using ONE list comprehension, create a list of squares 
# # of all odd numbers from 1 to 20.
# # Print the result.
odd = [n*n for n in range (1, 21) if n%2!= 0]
print(odd)
    