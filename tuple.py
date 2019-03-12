t = ('a', 'a', 'a', 'b', 'c')
mylist = [1, 2, 3]

print ( type(t))
print ( type(mylist))

print ( t[0])
print ( t.count('a'))
print ( t.index('c'))

# more examples - when to use it
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print (list_1)
print (list_2)

list_1[0] = 'Art'
print (list_1)
print (list_2)

# the value was changed in both lists
# read-only

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print (tuple_1)
print (tuple_2)

#tuple_1[0] = 'Art' # thrown an error - immutable

