from IPython.display import clear_output
def game_board(board):
    clear_output()
    print "  |"+"  |"+"   "
    print board[1]+" |"+board[2]+" |"+board[3]+"   "
    print "  |" + "  |" + "   "
    print "---------"
    print "  |" + "  |" + "   "
    print board[4] + " |" + board[5]+" |"+board[6]+"   "
    print "  |" + "  |" + "   "
    print "---------"
    print "  |" + "  |" + "   "
    print board[7] + " |" + board[8]+" |"+board[9]+"   "
    print "  |" + "  |" + "   "

# myboard=["X"]*10
# game_board(myboard)


import random
def choose_player():
    if random.randint(0,1)==0:
        return "player1_turn"
    else:
        return "player2_turn"
def player_input():
    player_inp=raw_input("Plese enter your choice(X/O): ")
    player_inp=player_inp.upper()
    if player_inp=="X":
        player1,player2=("X","O")
        return player1,player2
    elif player_inp=="O":
        player1,player2=("X","O")
        return player1,player2


def space_check(board,position):
    return board[position]==" "

##Enter Position
def choose_postition(board,player):
    position=0
    while position not in (1,2,3,4,5,6,7,8,9) or not space_check(board,position):
        position=int(input("{} Please enter Your Next Position: ".format(player)))
    return position
import random
def choose_postition2(board,player):
    position=0
    while position not in (1,2,3,4,5,6,7,8,9) or not space_check(board,position):
        position=random.randint(1,9)
    return position

###Place Marker
def place_marker(board,position,mark):
    board[position]=mark

###Won Checking
def won_check(board,mark):
   return ((board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] ==  mark and board[5] == mark and board[6] == mark) or (
                board[7] == mark and  board[8] == mark and  board[9] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (
                 board[2] == mark and  board[5] == mark and board[8] == mark) or (board[3] == mark and  board[6] == mark and board[9] == mark) or (
                 board[1] == mark and  board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark))
###Full Board Check
def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    else:
        return True
###Replay Game
import string
def replay():
    ascii_char=string.ascii_uppercase
    char=True

    while char:
        game=raw_input("Do you want to play again!! (Y/N): ")
        game=game.upper()

        if game not in ascii_char and game not in ("Y","N"):
            continue
        else:
            char=False

    return game=="Y"


while True:
    from IPython.display import clear_output
    print("Tic Tac Toe Game: ")
    my_board=[" "]*10
    player1,player2=player_input()
    turn=choose_player()
    user_input=raw_input("Do you want to play the game:[Y/N] ")
    user_input=user_input.upper()
    if user_input=="Y":
        gameon=True
    else:
        gameon=False
    if user_input=="Y":
        gameon=True
    else:
        gameon=False

    while gameon:
        clear_output()
        if turn=="Player1_turn":
            player1_position=choose_postition(my_board,player1)
            place_marker(my_board,player1_position,player1)
            game_board(my_board)
            print (won_check(my_board,player1))
            if won_check(my_board,player1)==True:
                print ("Congrats Player1 won the game")
                gameon=False
            else:
                if full_check(my_board)==True:
                    game_board(my_board)
                    print ("Game Tie")
                    break
                else:
                    turn="Player2_turn"
        else:
            clear_output()
            player2_position=choose_postition2(my_board,player2)
            place_marker(my_board,player2_position,player2)
            game_board(my_board)
            print (won_check(my_board, player2))
            if won_check(my_board,player2)==True:
                print ("Congrats Player2 won the game")
                gameon=False
            else:
                if full_check(my_board)==True:
                    game_board(my_board)
                    print ("Game Tie")
                    break
                else:
                    turn="Player1_turn"


    if not replay():
        break


