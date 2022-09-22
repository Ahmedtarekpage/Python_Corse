#Class : blueprint for creating new object
#Object : Instance of Class

#Class : Human
#object : John , Ahmed , Saud

#Instance Arrtibute → Attribue Object (كل كائن يختلف في ال att)
# Class Attribute → Is the Same for All Objects

class Point:
    default_color = "red" #Class Attribute
    def __init__(self, x, y): #Magical Method  Constructor
        self.x = x #Instance Attribute
        self.y = y


    def draw(self): #instance Method
        print(f"Point ({self.x}, {self.y})")

    @classmethod
    def zero(cls): #POINT Class
        return cls(0, 0)  #POINT(0,0)

point1 = Point(10, 4)
point2 = Point(3, 4)
print(point1)
print(type(point1))
print(isinstance(point1, int))
print(isinstance(point1,Point))
point1.draw()
point2.draw()

Point.default_color = "yellow"
print(point1.default_color)
print(Point.default_color)
print(point2.default_color)

point3 = Point.zero()  #(0,0)
point3.draw()