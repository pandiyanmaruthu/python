# from IPython.display import clear_output
# clear_output()
#
# print ("Hello Maruthu")
# clear_output()
# print ("\n"*5)
# clear_output()
# print ("Python")
# clear_output()
# import string
# print(string.ascii_uppercase)
from IPython.display import clear_output


def display_board(board):
    clear_output()
    print (board[1] + " |" + board[2] + "| " + board[3])
    print ("--|-|--")
    print (board[4] + " |" + board[5] + "| " + board[6])
    print ("--|-|--")
    print (board[7] + " |" + board[8] + "| " + board[9])

    # test_board1= ['#','X','O','X','O','X','O','X','O','X']
    test_board = [" "] * 10
    display_board(test_board)