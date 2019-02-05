mylist = [1,2,3,4,5,6,7,8,9,10]

print ("Elements of my list...: {}".format(mylist))
print ("Size of the list......: {}".format(len(mylist)))


# list elements of the list
#for i in mylist:
#    print (i)

# print if a number is even or odd
# print the sum of the list
'''
list_sum = 0

for number in mylist:
    if ( number % 2 == 0):
        print ("Number {} is an even number".format(number))
    else:
        print ("Number {} is an odd number".format(number))

    list_sum = list_sum + number

print ("Sum of the list is {}".format(list_sum))
'''

# iterating in a string
#mystring = 'Hello World'
#for i in mystring:
#    print (i)

# repeat a number of times without using the assigned variable
#for _ in mystring:
#    print ('Doing crazy stuff')


# using tupes
'''
mytuplist = [(1,2), (3,4), (5,6), (7,8)]
for item in mytuplist:
    print (item)

for a,b in mytuplist:
    print ( "X value {} and Y value {}".format(a,b))

'''

# loop througt dictionaries
mydict = {'id': 1, 
          'name': 'Alex', 
          'age': 40, 
          'address': '1020 Capstone CT',
          'city': 'Suwanee',
          'state': 'Georgia'
          }

# looping only for the keys
for item in mydict:
    print (item)

# looping throught key and values
for item in mydict.items():
    print (item)

for key,value in mydict.items():
    print ("Key is {} and value is {}".format(key,value))