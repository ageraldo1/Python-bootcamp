def new_decorator(original_function):

    def wrap_func():
        print ('I will be including some extra code BEFORE execute my original function')
        original_function()
        print ('I will be including some extra code AFTER execute my original function')

    return wrap_func

# on/off switch to wrap new features for your original function
# decorating the function with some extra code
# wide use for web framework
@new_decorator
def func_needs_decorator():
    print ("I want to be decorated!!!")    

#decorated_func = new_decorator(func_needs_decorator)    
#decorated_func()

func_needs_decorator()        
