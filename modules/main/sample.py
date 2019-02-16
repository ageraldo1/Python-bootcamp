def func_one():
    print ("Function one")

def func_two():
    print ("Function two")    


print (__name__)
if ( __name__ == "__main__"):
    print ("Running directly the one.py file")

    # run func_one()
    # run func_two()
    # flow control - commonly used to control the flow execution of your code
else:
    print ("One.py is a module that was imported")

