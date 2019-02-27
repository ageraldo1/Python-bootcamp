def create_cubes(number):
    result = []

    for i in range(number):
        result.append(i**3)

    return result

print (create_cubes(10))    

# example when you only need to value just one time instead of having the entire list in memory
# range function is a generator
# range(10)
# list(range(10))
for x in create_cubes(10):
    print (x)

# to fix the memory issue, let's rewrite the same function to be used as a generator
def create_cubes_generator(number):
    for i in range(number):
        yield (i**3)

print (create_cubes_generator(10))    
print (list(create_cubes_generator(10)))

for x in create_cubes_generator(10):
    print (x)

# example 2
def gen_finonbacci(n):

    a=1
    b=1

    for _ in range(n):
        yield a
        a,b = b,a+b

gen_finonbacci(10)        
print(list(gen_finonbacci(10)))

# example 3
def simple_gen():
    for x in range(3):
        yield x

g = simple_gen()
print (next(g))        
print (next(g))        
print (next(g)) 


# example 4
s = 'Hello'
s_iter = iter(s)
print (next(s_iter))



# example 5
my_numbers = [x*x for x in [1,2,3,4,5]]
print (my_numbers)

my_numbers = (x*x for x in [1,2,3,4,5])
print (my_numbers)
