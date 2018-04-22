### MyBoard
from IPython.display import clear_output
import os
def game_board(board):
    clear_output()
    clear=lambda :os.system('cls')
    clear
    print ("  |"+"  |"+"  |")
    print (" "+board[1]+" "+" "+board[2]+" "+" "+board[3]+" ")
    print ("  |" + "  |" + "  |")
    print ("---------")
    print ("  |" + "  |" + "  |")
    print (" " + board[4] + " " + " " + board[5] + " " + " " + board[6] + " ")
    print ("  |" + "  |" + "  |")
    print ("---------")
    print ("  |" + "  |" + "  |")
    print (" " + board[7] + " " + " " + board[8] + " " + " " + board[9] + " ")
    print ("  |" + "  |" + "  |")
    print ("---------")
# myboard=["X"]*10
# game_board(myboard)
# game_board(myboard)
### Player Marker
def marker(board,player,position):
    board[position]=player

### Space Check
def space_check(board,position):
    return board[position]==" "


### player position
def player_position(board):
    position=0
    while position not in (1,2,3,4,5,6,7,8,9) or not space_check(board,position):
        position=input("Please enter your position: ")
    return position
#### Player2 position
import random
def player_position2(board):
    position=0
    while position not in (1,2,3,4,5,6,7,8,9) or not space_check(board,position):
        position=random.randint(1,9)
    return position
### Game Won check
def won_check(board,mark):
     return ((board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark)
             or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8]) or (board[3] == mark and board[6] ==mark and board[9] == mark) or
             (board[1]==mark and board[5]==mark and board[9]==mark) or (board[3]==mark and board[5]==mark and board[7]==mark))
    #     return True
    # else:
    #     return False
    # return ((board[1] == mark and board[2] == mark and board[3] == mark) or (
    #             board[4] == mark and board[5] == mark and board[6] == mark) or (
    #                 board[7] == mark and board[8] == mark and board[9] == mark) or (
    #                     board[1] == mark and board[4] == mark and board[7] == mark) or (
    #                 board[2] == mark and board[5] == mark and board[8] == mark) or (
    #                     board[3] == mark and board[6] == mark and board[9] == mark) or (
    #                 board[1] == mark and board[5] == mark and board[9] == mark) or (
    #                     board[3] == mark and board[5] == mark and board[7] == mark))

### Full check
def full_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    else:
        return True



### player choice
def player_choice():
    my_choice=" "
    while my_choice not in ("X","O"):
        my_choice=raw_input("Please enter your choice X/O: ").upper()
        if my_choice=="X":
            player1,player2=("X","O")
            return player1,player2
        else:
            player1,player2=("O","X")
            return player1,player2

### Replay
def replay():
    play_again=raw_input("Do You Want to Play again: Y/N ").upper()
    return play_again=="Y"
def gameplay():

    print("Tic Tac Toe Game!!!")
    while True:
        myboard=[" "]*10
        player1,player2=player_choice()
        playing=raw_input("Do you want to play the game:(Y/N) ").upper()
        if playing=="Y":
            gameon=True
            turn="player1_turn"
        else:
            gameon=False
        while gameon:
            if turn=="player1_turn":
                player1_position=player_position(myboard)
                marker(myboard,player1,player1_position)
                game_board(myboard)
                if won_check(myboard,player1):
                    print ("Congrats Player1 Won the game")
                    gameon=False
                else:
                    if full_check(myboard)==True:
                        print ("Sorry Game Tie")
                    else:
                        turn="player2_turn"
            else:
                    player2_position = player_position2(myboard)
                    marker(myboard, player2, player2_position)
                    game_board(myboard)
                    if won_check(myboard, player2)==True:
                        print ("Congrats Player2 Won the game")
                        gameon = False
                    else:
                        if full_check(myboard):
                            print ("Sorry Game Tie")
                        else:
                            turn = "player1_turn"
        if not replay():
            break
gameplay()
