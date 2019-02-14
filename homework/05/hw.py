import math

class Line():
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        # x1,y1 = coord1
        # x2,y2 = coord2
        return math.sqrt(math.pow((self.coor2[0] - self.coor1[0]),2) + math.pow((self.coor2[1] - self.coor1[1]),2))
    
    def slope(self):
        return ((self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0]))

coordinate1 = (3,2)
coordinate2 = (8,10)

line = Line(coordinate1, coordinate2)
print (line.slope())
print (line.distance())


class Cylinder():
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return math.pi * math.pow(self.radius, 2) * self.height

    def surface_area(self):
        return (2 * math.pi * self.radius * self.height) + ( 2 * math.pi * math.pow(self.radius,2))

c = Cylinder(2,3) 
c.volume()
c.surface_area()       
