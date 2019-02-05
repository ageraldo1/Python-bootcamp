# Example 1
name = 'Alexandre Geraldo'

def printer():
    name = 'Someone else'
    print (name)

printer()  ## will print Alexandre Geraldo  
print (name)

# Example 2
# changing a global variable
x = 50

def test_function():
    global x  # avoid to use it, make the function return a value instead and re-assign the new value for the global variable

    print ( 'Local X value is {}'.format(x))

    x = x + 1

test_function()
print ('Global X value is {}'.format(x))