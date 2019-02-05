# map function
# example 1
def square(number):
    return number**2

my_list = [1,2,3,4,5]

# way 1
for item in map(square, my_list):
    print (item)

# way 2
print (list(map(square, my_list)))

# filter function
# example 1 
def check_even(num):
    return ( num % 2 == 0)

my_numbers = [1,2,3,4,5,6]    

print (list(filter(check_even, my_numbers)))

# lambda - anonymous function - one time only functions
#def square(num):
#    return num**2
#square(3)
# example 1
square = lambda num: num **2
square(3)

# example 2 using together with map
my_numbers = [1,2,3,4,5,6]
list(map(lambda num: num ** 2, my_numbers))

# example 3 using with filter
#lambda num: num % 2 == 0
list(filter(lambda num: num % 2 == 0, my_numbers))

# example 4
# note that after the lambda keyword, what is expected is the input name for the function
my_names = ['Alexandre', 'Dias', 'Geraldo']
list(map(lambda name: name[0], my_names)) # first letter
list(map(lambda name: name[::-1], my_names)) # reverse 


