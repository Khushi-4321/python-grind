students = {}

students["khushi"] = [89, 46, 76, 97, 65]
students["Tisha"] = [68, 64, 84, 76, 98]
students["Tejasvi"] = [98, 53, 86, 46, 69]

for name, marks in students.items():
    avg = sum(marks)/len(marks)
    grade = "A" if avg>= 85 else "B" if avg >=75 else "C" 
    print(f"{name} Average ={avg:.1f} Grade = {grade} ")

    topper = max(students, key = lambda x : sum(students[x]))
    print(f"Topper: {topper}")
