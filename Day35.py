students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 42},
    {"name": "Charlie", "marks": 91},
    {"name": "Diana", "marks": 55}
]

# Using map and lambda only (no filter):
# Return a new list of dictionaries with:
# - name as is
# - grade: "Pass" if marks >= 50 else "Fail"

result = list(map(lambda x: {"name": x["name"], "grade": "Pass" if x["marks"]>= 50 else "Fail"}, students))
print(result)
                