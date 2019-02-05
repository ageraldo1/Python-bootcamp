# range operator
'''
print ('Example 1 for range operator : defining a stop point')
for number in range(10):
    print (number)

print ('\nExample 2 for range operator : defining a start and stop point')
for number in range(3, 10):
    print (number)

print ('\nExample 3 for range operator : defining a start, stop and jump')
for number in range(0, 10, 2):
    print (number)


print ('\nExample 4 for range operator : casting')
print ( list(range(0,10)))
'''

#enumate function
'''
index_count = 0
word = 'abcdef'

print ('Example 1 for enumrate operator : old style')

for letter in word:
    print (word[index_count])
    index_count += 1

print ('Example 2 for enumrate operator : returns a tupe')

for item,letter in enumerate(word):
    print ('Item is {} and the letter is {}'.format(item, letter))
'''

'''
#zip function 
mylist1 = [ 1, 2, 3]
mylist2 = [ 'a', 'b', 'c']
mylist3 = [100, 200, 300]

for item in zip(mylist1, mylist2, mylist3):
    print (item)

# you can also cast the zip to a list
# list(zip(mylist1, mylist2, ....))
'''

# in operator ( exists )
'''
mylist = [1, 2, 3]
print ( 1 in mylist)
print ( 10 in mylist)

mystring = 'Hello World again....'
print ( 'I' in mystring)

mydict = {'key': 123}
print ( 'key' in mydict)
print ('key' in mydict.keys())
print ( 123 in mydict.values())
'''

'''
# min/max
mylist = list(range(0,100))
print (min(mylist))
print (max(mylist))
'''

# user input

result = input ("Enter a number :")
print ("The number is {}".format(result))
print (type(result))