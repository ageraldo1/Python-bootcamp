items = {'1': 'Pecan', 
         '2': 'Apple Crisp', 
         '3': 'Bean', 
         '4': 'Banoffee', 
         '5': 'Black Bun', 
         '6': 'Blueberry', 
         '7': 'Buko',
         '8': 'Burek',
         '9': 'Tamale',
         '10': 'Steak'
        }

item_totals = {}

print ("Welcome to the House of Pies! Here are our pies:\n")
for _ in range(50):
    print ("-", end="")

print ("\n")
for k,v in items.items():
    print (f"({k}) {v}   ", end="")
print ("\n") 

user_continue = "y"
total_orders = 0

while user_continue == "y":
    user_input = input("Please select a item : ")

    if user_input in items:
        print (f"\tGreat! We'll have that {items[user_input]} right out for you!")
        total_orders = total_orders + 1

        if user_input in item_totals:
            item_totals[user_input] = item_totals[user_input] + 1

        else:
            item_totals[user_input] = 1
    
    user_continue = input ("\nPlease type y to continue or press another key to quit ")

print (f"Total of items ordered : {total_orders}")

for k,v in items.items():
    if k in item_totals:
        print (f"{item_totals[k]} {v}")
    else:
        print (f"0 {v}")
1
