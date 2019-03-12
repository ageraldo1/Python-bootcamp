# example 1 - sort to a new variable - works for any iterable
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li)

print (li)
print (s_li)

# example 2 - sort in place - only works for list
li.sort()
print (li)

# example 3 - in reverse order
li.sort(reverse=True)
print (li)

# sorting a set
my_set = {8, 4, 99, 8, 4}
print (my_set)
print (sorted(my_set))

# tuples
tup = (9,1,8,2,7,3,6,4,5)
print (tup)
print (sorted(tup))

# dictionary
my_dict = {
    'name': 'Alex',
    'job': 'Programming',
    'age': 40,
    'os': 'Linux'
}

print (my_dict)
print (sorted(my_dict)) # sort only keys

# sort using condition
li = [-6, -5, -4, 1, 2, 3]
print ( sorted(li, key=abs))

# sorting a class
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return (f"{self.name}, {self.age}, ${self.salary}")

e1 = Employee('Alex', 37, 70000)
e2 = Employee('Joe', 29, 80000)
e3 = Employee('Max', 43, 90000)

employess = [e1, e2, e3]
print (employess)

def e_sort(emp):
    return emp.salary

print (sorted(employess, key=e_sort, reverse=True))
print (sorted(employess, key=lambda e: e.name, reverse=False))

# using operator module
from operator import attrgetter
print (sorted(employess, key=attrgetter('age'), reverse=False))

