def add_numbers(n1, n2):
    try:        
        print (int(n1)+int(n2))

    except:
        print ("Please use only integers")
    else:
        # there is no error
        pass

    finally:
        # with error or not the code below will be executed
        pass       

#number1 = 10
#number2 = input("Please enter a number..:")

#add_numbers(number1, number2)    


def ask_for_int():
    while True:        
        try:
            result = input("Please provide number:")
            result = int(result)

        except:
            print ("Invalid number !! {}".format(result))
            continue

        else:
            print ("Good job! Your number is {}".format(result))
            break

        finally:
            pass
            #print ("Function finished")

ask_for_int()