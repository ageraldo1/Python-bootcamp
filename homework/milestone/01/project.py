from game_libs import print_board, start_game, end_game, swap_players, game_info, pick, game_process, next_round

user_choice = ""

# main game loop
while game_info["state"] != "e":
    print_board()

    # game state
    if  game_info["state"] == "n":
        print("    Type [S] to start or [E] for exit")        

    elif game_info["state"] == "p":
        print ("Player{} needs to type a number between 1 and 9".format(game_info["current_player"]))

    # user choice
    user_choice = input("\n\nUser selection...: ")

    if (user_choice.lower() == "e"):
        end_game() 
        
    elif (user_choice.lower() == "s"):        
        start_game()        
    
    elif (user_choice.isnumeric() and game_info["state"] == "p"):
        if ( int(user_choice) in range(1, 10)):
            if (pick(int(user_choice))) == True:
                game_process()

                if game_info["current_round"] == "c":
                    swap_players()

                elif game_info["current_round"] == "w":
                    input ("Player {} win this round! Press any key to continue".format(game_info["current_player"]))
                    next_round()

                elif game_info["current_round"] == "t":
                    input ("Game tied!!! Press any key to continue")
                    next_round()
            else:
                 input ("Position {} already taken by another player. Press any key to continue".format(user_choice))  
        else:
            input ("Please type a valid number. Press any key to continue")    

    else:
        input ("Please type a valid option. Press any key to continue")
        

    
    

