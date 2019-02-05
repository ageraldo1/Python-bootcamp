# Example 1 - no parameters

def sample_function():
    '''
    DOCSTRING: Information about this function
    INPUT: no input
    OUTPUT: Hello message
    '''
    print ('Hello Sample Function')

#sample_function()    

# Example 2 - parameters and default value
def say_hello(name='Default Name'):
    print ('Hello {}'.format(name))

#say_hello()
#say_hello('Alex')    


# Exampe 3 - parameters and return value
def add_numbers(x = 0, y = 0 ):
    return x + y

#result = add_numbers ( 1, 2)
#print (result)    

#result = add_numbers (5)
#print (result)

#result = add_numbers ()
#print (result)


# Example 4 - find specific word in a string

def find_word(phrase='', word=''):

    return word.lower() in phrase.lower()

#print ( find_word('This is my phrase', 'this'))

def pig_latin(word=''):
    # if word in 'aeioi'
    vowel = ['a', 'e', 'i', 'o', 'u']

    for letter in vowel:
        if word.startswith(letter):
            return (word + 'ay')

    return word[1:] + word[0] + 'ay'

#print (pig_latin('word'))
#print (pig_latin('apple'))

# Exercise 1
def lesser_of_two_numbers(x, y):
    if ( x % 2 == 0) and ( y % 2 == 0):
        return (min(x,y))

    else:
        return (max(x,y))

#print ( lesser_of_two_numbers(2,4))        
#print ( lesser_of_two_numbers(2,5))        

# Exercise 2
def animal_crackers(text):
    first  = text.split(sep=' ')[0]
    second = text.split(sep=' ')[1]

    return ( first[0] == second[0])

#print (animal_crackers('Levelheaded Llama'))
#print (animal_crackers('Crazy Kangaroo'))

# Exercise 3
def makes_twenty(n1,n2):
    if ((( n1 == 20 ) or ( n2 == 20)) or (n1 + n2 == 20)):
        return True

    else:
        return False

#print (makes_twenty(20,10))     
#print (makes_twenty(12,8))
#print (makes_twenty(2,3))
   
# Exercise 4
def old_macdonald(name=''):
    return (name[0].upper() + name[1:3] + name[3].upper() + name[4:]) 

#print (old_macdonald('macdonald'))


# Exercise 5
def master_yoda(text):
    phrase = []
    phrase = text.split(sep=' ')
    phrase.reverse()

    # another way to reverse the list
    # return phrase[::-1]

    return ( ' '.join(phrase) )

    

#print (master_yoda('I am home'))   # --> 'home am I'
#print (master_yoda('We are ready'))        # --> 'ready are We'

# Exercise 6
# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200¶
def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

#print (almost_there(90))
#print (almost_there(104))
#print (almost_there(150))
#print (almost_there(209))


# Exercise 7
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums=[]):
    first = False

    for number in nums:
        if ( number == 3):
            if ( first == False):
                first = True

            else:
                return True
        else:
            first = False

    return False

# another way to write the function
# cannot consider the last element of the list - overflow
# for i in range(0, len(nums)-1):
#    if nums[i] == 3 and nums[i+1] == 3:
#        return True
#
#     return False
#print (has_33([1, 3, 3]))
#print (has_33([1, 3, 1, 3]))
#print (has_33([3, 1, 3]))


# Exercise 8
# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'

def paper_doll(text):
    #mylist = []
    mylist = ''

    for word in text:
        #mylist.append(word * 3)
        mylist += (word * 3)
    
    #return ''.join(mylist)
    return mylist

#print (paper_doll('Hello'))
#print (paper_doll('Mississippi'))

# Exercise 9
# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    # could use also the sum function - sum(a,b,c) <= 21
    if ( a + b + c ) <= 21:
        return a + b + c

    if ( a == 11 or b == 11 or c == 11):
        sum =  (a + b + c) - 10

        if ( sum > 21):
            return 'BUST'
        else:
            return sum
    else:
        return 'BUST'

#print (blackjack(5,6,7))
#print (blackjack(9,9,9))
#print (blackjack(9,9,11))


# Exercise 10
# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 
# and extending to the next 9 (every 6 will be followed by at least one 9). 
# Return 0 for no numbers
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    total = 0
    disable_sum = False

    for number in arr:

        if ( number == 6):
            disable_sum = True
            
        elif ( number == 9):
            disable_sum = False

        else:
            if ( disable_sum == False):
                total = total + number
    
    return total

#print (summer_69([1, 3, 5]))
#print (summer_69([4, 5, 6, 7, 8, 9]))
#print (summer_69([2, 1, 6, 9, 11]))


# Exercise 11
# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
#  spy_game([1,2,4,0,0,7,5]) --> True
#  spy_game([1,0,2,4,0,5,7]) --> True
#  spy_game([1,7,2,0,4,5,0]) --> False


def spy_game(nums):
    #secret_list = []

    #for number in nums:
    #    if (number == 0 or number == 7):
    #        secret_list.append(number)

    secret_list = [number for number in nums if (number == 0 or number == 7) ]

    if ( len(secret_list) == 3):
        return (secret_list == [0,0,7])
    else:
        return False

print (spy_game([1,2,4,0,0,7,5]))
print (spy_game([1,0,2,4,0,5,7]))
print (spy_game([1,7,2,0,4,5,0]))


# Exercise 12
# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
# count_primes(100) --> 25

def count_primes(num):
    
    total_primes = 0

    if ( num > 1):
        for number in range(2, num):
            #for is_prime is range(2, number):
            #    if ( is_prime %)
            #total_primes = total_primes + number

            print (number)

        return total_primes
    else:
        # less or equal to 1, the number is not prime
        return 0

    
print (count_primes(10))

