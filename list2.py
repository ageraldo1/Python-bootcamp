mystring = 'Hello'
mylist = []

for letter in mystring:
    mylist.append(letter)

print (mylist)    


# advanced list - getting rid of append
mylist2 = [x for x in mystring]
print (mylist2)


mynumberlist = [ number for number in range(0,10)]
print (mynumberlist)

mysquarelist = [ number**2 for number in range(0,10)]
print (mysquarelist)


myevenlist = [ number for number in range(0,11) if ( number % 2 == 0)]
print (myevenlist)


celcius = [0, 10, 21.5, 34.5, 45.0, 43.4]
fahrenheit = [ ((9/5)*temp + 32) for temp in celcius ]

print ("Temperature in celcius......: {}".format(celcius))
print ("Temperature in fahrenheit...: {}".format(fahrenheit))

# same as :
fahrenheit = []

for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))

print ("Temperature in fahrenheit...: {}".format(fahrenheit))    