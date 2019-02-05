# Example 1
def sumNumbers(*args):
    # args is a tuple
    return sum(args) * 0.05


#print ( sumNumbers(60,40))    
#print ( sumNumbers(60,40,100)) 
#print ( sumNumbers(60,40,100,100)) 

# Example 2
def sample_args(*args):
    for item in args:
        print ("The passed argument is equal to {}".format(item))

sample_args(1,2,3,4,5)        


# Example 3
def sample_kwargs(**kwargs):
    # kwargs is a dictionary, key and word value

    if "fruit" in kwargs:
        print ('My favorite fruit is {}'.format(kwargs['fruit']))
    else:
        print ('You dont like anything')


sample_kwargs(fruit='apple', veggie='tomato')    
sample_kwargs(drink='wine', food='salmon')    


# Example 4
#def myfunc(*args):
#    return [ number for number in args if ( number % 2 == 0)]

def myfunc(name):
    even=False
    newlist = []

    for word in name:
        if (even == True):
            newlist.append(word.upper())
            even = False
        else:
            newlist.append(word.lower())
            even = True 

    return str(newlist)

print (myfunc('Antho'))
