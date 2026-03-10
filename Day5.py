# Create a file called "students.txt"
# Write 3 student names and their marks (one per line)
# Read it back and print each line

with open ("student.txt", "w") as f:
    f.write("Khushi, marks = 97\n")
    f.write("Tisha, marks = 94\n")
    f.write("Moksh, marks = 61\n")

with open("student.txt", "r") as f:
    content = f.read()
    print(content)
