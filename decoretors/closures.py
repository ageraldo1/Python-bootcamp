# example 1
def outer_func():
    message = 'Hi outer_func!'

    def inner_func():
        print (message)

    return inner_func()

outer_func()

# example 2
# inner function still have access to a var defined out of scope
def outer_func(msg):
    message = msg

    def inner_func():
        print (message)

    return inner_func

my_hi_func = outer_func('Hi my_hi_func')
my_hello_func = outer_func('Hi my_hello_func')

my_hi_func()
my_hello_func()


