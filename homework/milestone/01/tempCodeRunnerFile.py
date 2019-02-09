from game_libs import print_board

game_state = "new"          # new, playing, ended

# main game loop
while game_state != "ended":
    print_board()

    if game_state == "new":
        user_choice = input("    Type [S] to start or [E] for exit")

    print ("User Choice...: {}".format(user_choice))
    

