# rock -> scissor -> paper -> rock
#
import random

game_rules = {
    "r": "s",
    "s": "p",
    "p": "r"
}

element_names = {
    "r": "Rock",
    "s": "Scissor",
    "p": "Paper"
}

user_option = ""
rnd_choices = ['r', 's', 'p']

while user_option != "e":
    user_option = input("Please type [r] to rock, [s] to scissor, [p] paper or [e] to exit the game : ")

    if user_option in rnd_choices:
        rnd_option = random.choice(rnd_choices)

        if ( game_rules[user_option] == rnd_option):
            print ("\tUser won the game - your choice {} and computer choice {}\n".format(element_names[user_option], element_names[rnd_option]))

        elif (game_rules[rnd_option] == user_option):
            print ("\tComputer won the game - your choice {} and computer choice {}\n".format(element_names[user_option], element_names[rnd_option]))

        else:
            print ("\tGame tied - your choice {} and computer choice {}\n".format(element_names[user_option], element_names[rnd_option]))

    
