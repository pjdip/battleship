from random import randint
import sys

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def get_guess():
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
    return guess_row, guess_col

def get_board_size():
    guess_row = int(raw_input("Guess Row: "))
    guess_col = int(raw_input("Guess Col: "))
    return guess_row, guess_col

def check_hit(board, row_ship, row_guess, col_ship, col_guess, size_board):
    if row_guess == row_ship and col_guess == col_ship:
        print "\nCongratulations! You sank my battleship!\n"
        board[row_guess][col_guess] = "X"
        return True
    else:
        if row_guess not in range(size_board) or \
            col_guess not in range(size_board):
            print "\nOops, that's not even in the ocean."
        elif board[row_guess][col_guess] == "X":
            print "\nYou guessed that one already."
        else:
            print "\nYou missed my battleship!"
            board[row_guess][col_guess] = "X"
        print "Please guess again\n"
    print_board(board)
    print
    return board

def would_continue():
    to_continue = raw_input("Would you like to continue? respond Y or N: ")
    if to_continue == "N" or to_continue == "n":
        sys.exit()

def ship_num(board_dimension):
    print "You will now choose a difficulty for the game"
    print "Pick a decimal between 0 - 1 to decide how many hits/misses there will be"
    print "Closer to 0 means less hits, closer to 1 means more hits"
    difficulty = float(raw_input("give a number between 0 and 1: "))
    num_ships = difficulty * (board_dimension ** 2)
    return int(num_ships)

def find_new_ship(board):
    ship_row = random_row(board)
    ship_col = random_col(board)
    ship_location = [ship_row, ship_col]
    return ship_location

def ship_list(no_ships, board):
    list_of_ships = []
    for ship in range(no_ships):
        ship_location = find_new_ship(board)
        while ship_location in list_of_ships:
            ship_location = find_new_ship(board)
        list_of_ships.append(ship_location)
    print list_of_ships
    return list_of_ships

def main():
    board = []
    board_size = int(raw_input("\nSize of board please: "))

    ship_no = ship_num(board_size)
    print ship_no

    for x in range(0, board_size):
        board.append(["O"] * board_size)

    ship_list(ship_no, board)

    ship_row = random_row(board)
    ship_col = random_col(board)
    print ship_row, ship_col

    guess_row, guess_col = get_guess()

#@todo need to change check_hit to take in ship_list
#@todo how many ships are left to hit instead of quitting after hitting one
    guess_hit = check_hit(board, ship_row, guess_row, ship_col, guess_col, board_size)

    while guess_hit != True:
        would_continue()
        print "just a reminder, the ship is at coord: ", ship_row, ship_col
        guess_row, guess_col = get_guess()
        guess_hit = check_hit(board, ship_row, guess_row, ship_col, guess_col, board_size)

    print_board(board)

main()
