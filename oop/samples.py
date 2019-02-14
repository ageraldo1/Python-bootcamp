class Dog():

    species = 'mammal'

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots

    def bark(self):
        print ('WOOF!!!! {} is my name'.format(self.name.capitalize()))

my_dog = Dog(breed='vira-lata', name='spike', spots=False)

type(my_dog)
print (my_dog.breed)
print (my_dog.species)
my_dog.bark()

import math

class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = Circle.pi * math.pow(radius, 2)

    def get_circumference(self):
        return 2 * Circle.pi * self.radius

my_circle = Circle()
print (my_circle.get_circumference())
print (my_circle.area)
