from IPython.display import clear_output


def display_board(board):
    clear_output()
    print (board[1] + " |" + board[2] + "| " + board[3])
    print ("--|-|--")
    print (board[4] + " |" + board[5] + "| " + board[6])
    print ("--|-|--")
    print (board[7] + " |" + board[8] + "| " + board[9])

# test_board=[" "]*10
# display_board(test_board)
import string
def player_input():
    alpha = string.ascii_uppercase
    while True:
        #         alpha=string.ascii_uppercase
        #     print (alpha)
        player1 = raw_input("Please Enter your choice'(X|O)':")
        player1 = player1.upper()
        if (player1 not in alpha) or (player1 not in ("X", "O")):
            continue
        elif player1 == "X":
            player1, player2 = ("X", "O")
            return player1,player2
        else:
            player2, player1 = ("O", "X")
            return player1,player2
# player1,player2=player_input()
# print (player2)
def place_marker(board, marker, position):
    # display_board(board)
    board[position]=marker
    return board[position]
# place_marker(test_board,'$',8)
# display_board(test_board)
def win_check(board, mark):
    if ((board[1] == board[2] == board[3]) == mark and (board[4] == board[5] == board[6]) == mark and (board[7] == board[8] == board[9]) == mark and (board[1] == board[4] == board[7]) == mark and (board[2] == board[5] == board[8]) == mark (board[3] == board[6] == board[9]) == mark and (board[1] == board[5] == board[9]) == mark and (board[3] == board[5] == board[7]) == mark):
        if mark=="X":
            return "player1"
        elif mark=="O":
            return "player2"
import random

def choose_first():
    # choice=random.randint(1,2)
    # if choice==1:
    #     return "play1"
    # else:
    #     return "play2"
    choice=raw_input("Who's going to start (X or O): ")
    if choice=="X":
        return "play1"
    elif choice=="O":
        return "play2"

def space_check(board, position):
    # for i in range(1,10):
    if board[position]!=" ":
        return True




def full_board_check(board):
    if " " not in board:
        return True
    else:
        return False


def player_choice():
    choice_player1 = input("Plese enter Your next Position(1-9): ")

    return choice_player1


def replay():
    playagain = raw_input("Do you want to play again (Y/N) : ")
    playagain=playagain.upper()
    if playagain == "Y":
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')
test_board = [" "] * 10
while True:
    # Set the game up here
    # pass
    #     test_board=[" "]*10
    clear_output()
    display_board(test_board)
    player1, player2 = player_input()
    #     choice_player1=player_choice(test_board)
    #     place_marker(test_board,player1,position)
    #     choose_first()
    #     display_board(test_board)
    print ("Test")
    start = choose_first()
    if start == "play1":
        start = "1player"
    else:
        start = "2player"

    # while game_on:
    while True:
        # Player 1 Turn
        clear_output()
        if start == "1player":
            choice_player1 = player_choice()
            if space_check(test_board, choice_player1) ==True:
                continue


            place_marker(test_board, player1, choice_player1)
            display_board(test_board)
            if win_check(test_board, player1)=="player1":
                print ("{}".format("Player1 Won"))
                break

            start = "2player"

        # Player2's turn.
        if start == "2player":
            choice_player2 = random.randint(1, 9)
            if space_check(test_board, choice_player2)==True:
                continue


            place_marker(test_board, player2, choice_player2)

            # win_check(test_board, player2)
            if win_check(test_board, player2)=="player2":
                print ("{}".format("Player2 Won"))
                break



        if full_board_check(test_board)==True:
            break

    # if not replay():
    if replay()==True:
        continue
    else:
        break
    # break


