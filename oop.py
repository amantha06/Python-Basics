import math

class Animal():
    def __init__(self):
        print("Animal Created")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    
    def distance(self):
        
        x1,y1 = self.coor1
        x2,y2 = self.coor2

        return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

    def slope(self):
       
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        
        return (y2 - y1)/(x2 - x1)

class Cylinder():
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):

        return self.height * math.pi * (self.radius)**2
    
    def surface_area(self):

        top = math.pi * (self.radius ** 2)
        return (top*2) + (2*math.pi*self.radius*self.height)


myanimal = Animal()
myanimal.who_am_i()
myanimal.eat()
mydog = Dog()
mydog.eat()
c1 = (3,2)
c2 = (8,10)

myline = Line(c1,c2)
print(myline.distance())

mycyl = Cylinder(2,3)
print(mycyl.volume())
print(mycyl.surface_area())
