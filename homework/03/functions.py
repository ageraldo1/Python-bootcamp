import math

# hw 1
def vol(rad):
    return ((4/3) * math.pi * pow(rad, 3))

print (vol(2))

# hw 2
def ran_check(num,low,high):
    # return num in range(low,high)
    return ( num >= low and num <= high)

ran_check(5,2,7)


# hw 3
def up_low(s):
    print ("Original String : {}".format(s))

    total_upper = 0
    total_lower = 0

    for letter in s:
        if ( letter.isalpha()):
            if ( letter.isupper()):
                total_upper = total_upper + 1
            else:
                total_lower = total_lower + 1
    
    print ("No. of Upper case characters : {}".format(total_upper))
    print ("No. of Lower case characters : {}".format(total_lower))

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

# hw 4
def unique_list(lst):
    u_set = set()

    for item in lst:
        u_set.add(item)
    
    return (list(u_set))
        
unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

# hw 5
def multiply(numbers):
    result = 0

    if ( len(numbers) > 0):
        result = numbers[0]

        for item in numbers[1::]:
            result = result * item
    
    return result

multiply([1,2,3,-4])

# hw 6
def palindrome(s):
    reverse = s[::-1]

    return ( s == reverse )

palindrome('helleh')
palindrome('madam')
    
# hw 7
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    phrase = set()

    for letter in str1:
        if ( letter.isalpha()):
            phrase.add(letter.lower())

    #return ( ''.join(sorted(phrase)) == alphabet)
    return ( sorted(phrase) == sorted(set(alphabet)))


ispangram("The quick brown fox jumps over the lazy dog")
ispangram("Alexandre Geraldo")
