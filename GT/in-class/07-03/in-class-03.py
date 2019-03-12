candies = {
    '0': 'Snickers', 
    '1': 'AirHeads', 
    '2': 'Cow Tales', 
    '3': 'Kit Kat', 
    '4': 'Chocolate'
}

allowance = 3
candyCart = []

for _ in range(allowance):
    for k,v in candies.items():
        print (f"[{k}] {v}")

    user_input = input("\nPlease select a candy : ")

    if user_input in candies:
        candyCart.append(candies[user_input])
    else:
        print ("Invalid choice!")

print ("\tYour Selection : ", end="")

for item in candyCart:
    print (f"{item} ", end="") 

print ("\n")
    
# courses = ['History', 'Math', 'Physics', 'CompSci']
#
# for index, course in enumare(courses):
#       print (index, course)
#

# s = " - ".join(courses)