# Create a class Shape with:
# - method: area() — returns 0

# Create two child classes:
# - Rectangle(Shape) — attributes: length, width — area() returns length * width
# - Circle(Shape) — attribute: radius — area() returns 3.14 * radius * radius

# Create one Rectangle and one Circle object.
# Print their areas with a label.

class shape:

    # def __init__(self, shape):
        # self.shape = shape
    def area(self):
    # print(f"Area:{area}")
        return 0

class Rectangle (shape):
    def __init__(self,length, width):
        self.length = length
        self.width = width
    def area(self):    
       return self.length * self.width

class Circle (shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius        

r = Rectangle(5,4)
c = Circle(7)

print(r.area())
print(c.area())
