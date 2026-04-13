# You have a list of students:
# 1. Use filter to get students who passed (marks >= 50)
# 2. Use map to extract just their names from the filtered list
# 3. Do it in one nested line

students = [
     {"name": "Alice", "marks": 85},
     {"name": "Bob", "marks": 42},
     {"name": "Charlie", "marks": 91},
     {"name": "Diana", "marks": 55}
 ]

passed = list(map(lambda x: x["name"], list(filter(lambda x: x["marks"] >=50, students)) ))
print(passed)