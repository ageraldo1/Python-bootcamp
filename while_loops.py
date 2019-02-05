'''
x = 0

while ( x < 10):
    print ( "X value is {} and it is less than 10".format(x) )
    x = x + 1   # x += 1
else:
    print ("X value is {} and it is no longer less than 10".format(x))

'''
# pass, continue and break usage

mylist = [1, 2, 3]
for number in mylist:
    # comment for do nothing
    pass

print ( "End of the for loop")


mystring = 'Hello World'
'''
for letter in mystring:
    if ( letter == 'l'):
        continue # ignore letter l. It makes the pointer jumps to the top of the loop
    
    print (letter)
'''

print ("Usage of break")
for letter in mystring:
    if (letter == 'o'):
        break
    print (letter)        