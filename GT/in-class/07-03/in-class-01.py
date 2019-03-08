print ("Hello User!")
user_name = input("What is your name? ")

if len(user_name) > 0:
    print (f"Hello {user_name}")
else:
    print ("Invalid name!")    

user_age = input("What is your age ?")

if user_age.isnumeric():
    if int(user_age) > 35:
        print ("Ah... A well traveled soul are ye.")
    else:
        print ("Awww... you're just a baby!")
else:
    print ("Invalid age!")        


