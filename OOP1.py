#Class : blueprint for creating new object
#Object : Instance of Class

#Class : Human
#object : John , Ahmed , Saud

class Point:
    def __init__(self, x, y): #Magical Method  Constructor
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

point1 = Point(10, 4)
point2 = Point(3, 4)
print(type(point1))
print(isinstance(point1, int))
print(isinstance(point1,Point))
point1.draw()
point2.draw()