# File handling basics
with open("test.txt", "w") as f:
    f.write("Hello, Khushi!\n")
    f.write("File handling started.\n")

with open("test.txt", "r") as f:
    print(f.read())