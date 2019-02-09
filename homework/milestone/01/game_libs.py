# main library functions
import os

# data structures
board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # global board list

score = { 
    "player1": 0,
    "player2": 0
}

game_info = {
    "state": "n",
    "current_player": 0,
    "current_round": "c"
}

# game functions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board():
    clear()
    print ("#=====================================#")
    print ("              Tic Tac Toe             ")
    print ("                 Game                 ")
    print ("#=====================================#")
    print ("          +-----+-----+-----+          ")
    print ("          |     |     |     |          ")
    print ("          |  {}  |  {}  |  {}  |       ".format(board[0],board[1], board[2]))
    print ("          |_____|_____|_____|")
    print ("          |     |     |     |")
    print ("          |  {}  |  {}  |  {}  |       ".format(board[3],board[4], board[5]))
    print ("          |_____|_____|_____|")
    print ("          |     |     |     |          ")
    print ("          |  {}  |  {}  |  {}  |       ".format(board[6],board[7], board[8]))
    print ("          |     |     |     |          ")
    print ("          +-----+-----+-----+")
    print ("")
    print ("      Player 1 [X]    Player 2 [O]")
    print ("")

def end_game():
    print ("\n#=====================================#")
    print ("              Final score")
    print ("#=====================================#")
    print ("Player 1....: {} win(s)".format(score["player1"]))
    print ("Player 2....: {} win(s)".format(score["player2"]))

    game_info["state"] = "e"

def start_game():
    score["player1"] = 0 
    score["player2"] = 0

    game_info["state"] = "p"
    game_info["current_player"] = 1

    reset_board()
   
def reset_board():
    board.clear()

    for i in range(1, 10):
        board.append(str(i))

def swap_players():    
    if ( game_info["current_player"] == 1):            
         game_info["current_player"] = 2

    else:
         game_info["current_player"] = 1

def pick(position):
    if ( board[position - 1].isnumeric()):
        if ( game_info["current_player"] == 1):
            board[position - 1] = "X"
        else:
            board[position - 1] = "O"

        return True
    else:
        return False

def next_round():
    game_info["current_player"] = 1
    game_info["current_round"] = "c"

    reset_board()
    

def game_process():
    sequence = ['0|3|6', '1|4|7', '2|5|8', '0|1|2', '3|4|5', '6|7|8', '0|4|8', '2|4|6']
    points = set()

    if tied() ==  True:
        game_info["current_round"] = "t"

    else:
        for item in sequence:
            for point in item.split(sep='|'):
                points.add(board[int(point)])
            
            if len(points) == 1:
                winner = "player" + str(game_info["current_player"])

                game_info["current_round"] = "w"            
                score[winner] = score[winner] + 1
                break
            
            points.clear()

def tied():
    for position in board:
        if position.isnumeric():
            return False

    return True        




