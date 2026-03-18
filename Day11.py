# Create a class Shape with:
# - method: area() — returns 0

# Create two child classes:
# - Rectangle(Shape) — attributes: length, width — area() returns length * width
# - Circle(Shape) — attribute: radius — area() returns 3.14 * radius * radius

# Create one Rectangle and one Circle object.
# Print their areas with a label.

class area:
    def __init__(self, shape):
        self.shape = shape
        def area(self):
            print(f"Area:{area}")

class Rectangle (area):
    def area(self,length, width):
        area = length * width

class Circle (area):
    def area(radius):
        area = 3.14 * radius * radius        

r = Rectangle(5,4)
c = Circle(7)

print(r.area)
print(c.area)
