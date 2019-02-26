# exercise 1
try:
    for i in ['a','b','c']:
        print(i**2)

except TypeError:
    print ("What you're trying to do make no sense")

# exercise 2
x = 5
y = 0

try:
    z = x/y

except ZeroDivisionError:
    print ("You cannot divide a number by zero")

finally:
    print ("All done")


# exercise 3
def ask():

    while True:
        try:
            result = input("Input an integer : ")
            result = int(result)

        except:
            print ("An error occurred! The number {} is invalid ! Please try it again".format(result))
            continue

        else:
            print ("Thank you, your number squared is : {}".format(result*result))
            break

    #print (result) -> variable still available....

ask()