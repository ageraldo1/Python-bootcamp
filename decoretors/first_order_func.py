# returning a value to a function
def square(number):
    return number * number

result = square(5)
print (square) 
print (result)   

# passing the function to the variable
# first-class function
result = square

print (square)
print (result)
print (result(5))


# passing functions as arguments
def cube(number):
    return number * number * number

def my_map(func, arg_list):
    result = []

    for i in arg_list:
        result.append(func(i))

    return result

squares = my_map(square, [1,2,3,4,5])
print (squares)

print (my_map(cube, [1,2,3,4,5]))

## returning functions
def logger(msg=''):

    def log_message():
        print ('Log message : {}'.format(msg) )
    
    return log_message

log_hi = logger('Hi')

log_hi()

# example 2
def html_tag(tag_name):

    def wrap_text(msg):
        print ('<{0}>{1}</{0}>'.format(tag_name,msg))
    
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test 1 headline!')
print_h1('Test 2 headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')
