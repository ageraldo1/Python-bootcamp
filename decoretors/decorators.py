# decorator_function -> outer_function
# wrapper_function   -> inner_function
def decorator_function(original_function):
    print ("Inside of decorator_function calling the function {}".format(original_function.__name__))
    def wrapper_function(*args, **kwargs):
        return original_function(*args, **kwargs)
    
    return wrapper_function

def display():
    print ('display function executed')    

decorated_display = decorator_function(display) 
decorated_display()   

# same result but using @sintax
@decorator_function
def display2():
    print ('display2 function executed')    

display2()

@decorator_function
def display_info(name, age):
    print ("display_info ran with arguments {} and {}".format(name,age))

display_info('Alex', 40)    