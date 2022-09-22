#Magical Methods
class Point:
    default_color = "red" #Class Attribute
    def __init__(self, x, y): #Magical Method  Constructor
        self.x = x #Instance Attribute
        self.y = y

    def __str__(self):
        return f"Point ({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    # def draw(self): #instance Method
    #     print(f"Point ({self.x}, {self.y})")

point1 = Point(10, 20)
print(point1)

other = Point(3, 4)
print(point1 == other)
print(point1 > other)
print(point1 + other)