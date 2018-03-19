from random import randint
import sys

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def get_guess():
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    return guess_row, guess_col

def get_board_size():
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    return guess_row, guess_col

def check_hit(board, row_ship, row_guess, col_ship, col_guess, size_board):
    if row_guess == row_ship and col_guess == col_ship:
        print("\nCongratulations! You sank my battleship!\n")
        board[row_guess][col_guess] = "X"
        return True
    else:
        if row_guess not in range(size_board) or \
            col_guess not in range(size_board):
            print("\nOops, that's not even in the ocean.")
        elif board[row_guess][col_guess] == "X":
            print("\nYou guessed that one already.")
        else:
            print("\nYou missed my battleship!")
            board[row_guess][col_guess] = "X"
        print("Please guess again\n")
    print_board(board)
    print("\n")
    return board

def would_continue():
    to_continue = input("Would you like to continue? respond Y or N: ")
    if to_continue == "N" or to_continue == "n":
        sys.exit()

def main():
    board = []
    board_size = int(input("\nSize of board please: "))

    for x in range(0, board_size):
        board.append(["O"] * board_size)

    ship_row = random_row(board)
    ship_col = random_col(board)
    print(ship_row, ship_col)

    guess_row, guess_col = get_guess()

    guess_hit = check_hit(board, ship_row, guess_row, ship_col, guess_col, board_size)

    while guess_hit != True:
        would_continue()
        print("just a reminder, the ship is at coord: ", ship_row, ship_col)
        guess_row, guess_col = get_guess()
        guess_hit = check_hit(board, ship_row, guess_row, ship_col, guess_col, board_size)

    print_board(board)

"""    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sank my battleship!"
        board[guess_row][guess_col] = "X"
    else:
        if guess_row not in range(5) or \
            guess_col not in range(5):
            print "Oops, that's not even in the ocean."
        elif board[guess_row][guess_col] == "X":
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        print "Please guess again"
"""

main()
