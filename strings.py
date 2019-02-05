myName = "Alex Geraldo"
sample1 = "I'm going to somewhere"
sample2 = "I'm going to \nsomewhere"

myString = "Hello World"

#print ( myName)
#print ( sample1)
#print ( sample2)
#print ( len(myName))


print ( myString)
print ( myString[0])
print ( myString[0:5])

print ( myString[-1])


print ( myString[:5])
print ( myString[6:])

s_string = 'abcdefghij'
print ( s_string[1:3])   # bc - stop position is not included
print ( s_string[::3])   # jump
print ( s_string[::-1])  # reverse string

name = "Sam"
last_letters = name[1:]
print ( 'P' + last_letters)  # concat

letter = "z"
print ( letter * 10)

print ( myName.upper())
print ( myString.split() )
