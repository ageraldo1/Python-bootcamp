nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# example 1
# loop way
my_list = []

for n in nums:
    my_list.append(n)

print (my_list)

# using list comprehension
my_list = [n for n in nums]
#          | |
#          | |_____________ for loop
#          |_______________ returing
#
print (my_list)


# example 2
# square a number
my_list = []
for n in nums:
    my_list.append(n**2)

print (my_list)

# using list comprehension
my_list = [(n**2) for n in nums]
#          |      |
#          |      |_____________ for loop
#          |
#          |____________________ returing. The expression that we want back
#
print (my_list)

# using map function
#my_list = map(lambda n: n*n, nums)

# using conditions
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)

print (my_list)

# using list comprehension
my_list = [(n) for n in nums if n % 2 == 0]
#          |   |             |
#          |   |             |_______________ conditional statement
#          |   |
#          |   |_____________________________ for loop
#          |
#          |_________________________________ returing. The expression that we want back
#
print (my_list)
# using filter function
# my_list = filter(lambda n: n%2 ==0, nums)

# example 4
my_list = []
for letter in 'abc':
    for num in range(3):
        my_list.append((letter, num))

print (my_list)
# using list comprehension
my_list = [(letter, num) for letter in 'abc' for num in range(3)]
#          |             |                   |
#          |             |                   |_____________ for loop 1
#          |             |
#          |             |_________________________________ for loop 2
#          |            
#          |_______________________________________________ returing. The expression that we want back (tuple)
#
print (my_list)


# example 5
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
#print (tuple(zip(names, heros)))

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero

print (my_dict) 

my_dict = {name: hero for name,hero in zip(names, heros)}
print (my_dict)

my_dict = {name: hero for name,hero in zip(names, heros) if name != 'Peter'}
print (my_dict)


# example 6
nums = [1,1,2,1,3,4,5,4,5,5,6,7,8,7,9,9]
my_set = set()

for n in nums:
    my_set.add(n)

print (nums)
print (my_set)

my_set = (n for n in nums)  # returns a generator

for i in set(my_set):
    print (i)
