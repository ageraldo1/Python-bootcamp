# 1
#Use for, .split(), and if to create a Statement that will print out words that start with 's':
print ("\nTask #1")
st = 'Print only the words that start with s in this sentence'
for word in st.split(sep=' '):
    if ( word.startswith('s')):
        print (word)


#2 Use range() to print all the even numbers from 0 to 10.
print ("\nTask #2")
for number in range(0,11):
    if ( number % 2 == 0):
        print (number)
# another way list (range(0,11,2))


# 3 Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print ("\nTask #3")

mylist = [number for number in range(1,51) if (number % 3 == 0)]
print ("My list is equal to {}".format(mylist)) 


#4 Go through the string below and if the length of a word is even print "even!"
print ("\nTask #4")

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split(sep=' '):
    if ( len(word) % 2 == 0):
        print ("Word {} is even".format(word))
    else:
        print (word)


# 5
# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".


print ("\nTask #5")
for number in range(1,101):

    if ( number % 3 == 0) and ( number % 5 == 0 ):
        print ("Number {} is FizzBuzz".format(number))

    elif ( number % 3 == 0):
        print ("Number {} is Fizz".format(number))

    elif ( number % 5 == 0):
        print ("Number {} is Buzz".format(number))

    else:
        print (number)

# 6 Use List Comprehension to create a list of the first letters of every word in the string below:
print ("\nTask #6")

st = 'Create a list of the first letters of every word in this string'

#mylist = [x for x in st.split(sep=' ')[0]]
#print (mylist)

mylist = []
for firstLetter in st.split(sep=' '):
    mylist.append (firstLetter[0])
print (st)
print (mylist)


mylist = [firstLetter[0] for firstLetter in st.split(sep=' ')]
print (mylist)

help(mylist.append)
