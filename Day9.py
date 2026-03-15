# reate a class called Student with:
# - attributes: name, marks (list of 5 subjects)
# - methods:
#     average() — returns average marks
#     grade() — returns "A" if avg >= 80, "B" if >= 60, else "C"
#     display() — prints name, average, grade

class student: 

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return sum(self.marks)/len(self.marks)    

    def grade(self): 
        if self.average() >= 80:
            return "A"
        elif self.average() >= 60:
            return "B"  
    
        else:
            return "C"
        

    def display(self):    
        print(f"{self.name}, {self.average()}, {self.grade()}")

s1 = student("Khushi", [79,54,67,83,58])
s1.display()
s2 = student("Tisha", [86,93, 88, 48, 75])
s2.display()