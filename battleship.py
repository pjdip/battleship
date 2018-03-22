from random import randint
import sys

# Let's the user know what this jam is all about
def print_greeting():
    print("\nThis is a game of battleship.")
    print("You will first decide the size of the board")
    print("The board will be square, you choose the dimension")

# A function that takes in the board as an argument and prints it
def print_board(board):
    print("\nHere is your board:\n")
    for row in board:
        print(" ".join(row))

# A function that takes in the dimension of the board
# and returns the users guess of ship location
# prompts the user for a guess as to location of ships
def get_guess(size_board):
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))
    # If the guess is outside the dimension of the board, ask again
    while guess_row not in range(size_board) or \
        guess_col not in range(size_board):
        print("\nOops, that's not even in the ocean.")
        print("Please guess again\n")
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))
    else:
        return [guess_row, guess_col]

# A function that takes in 4 arguments
# 1) the board itself 2) a list containing all coordinates that have been guessed
# 3) a list containing all ship coordinates 4) board dimension
# Checks if a guess is at the same coord as a ship
# Returns true if all ships are sunk
# Alters the board for hits and misses
# Removes ships from list of ships as they are hit
def check_hit(board, list_guesses, list_ships, size_board):
    # Checking the most recent guess, or last guess in guess list
    guess = list_guesses[-1]
    row_guess, col_guess = guess[0], guess[1]
    # If the guess shares a location with a ship
    if guess in list_ships:
        # Remove the ship from the list of ships
        list_ships.remove(guess)
        # If there are no more ships
        if list_ships == []:
            print("\nCongratulations! You sank all my ships! :P\n")
            board[row_guess][col_guess] = "B"
            return True
        else:
            print("\nCongratulations! You sank my battleship!\n")
            board[row_guess][col_guess] = "B"
    else:
        board[row_guess][col_guess] = "X"
        print("\nYou missed my battleship!")
        print("Please guess again\n")
    print_board(board)
    print
#    return board

# A function that checks if the user wants to keep playing
def would_continue():
    to_continue = input("Would you like to continue? respond Y or N: ")
    if to_continue == "N" or to_continue == "n":
        sys.exit()

# A function that takes in the size of the board as an arguments
# Asks user if they want there to be a lot of ships
# Returns the number of ships
#@todo could just ask user how many ships they want
def ship_num(board_dimension):
    print("\nYou will now choose a difficulty for the game")
    print("Pick a decimal between 0 - 1 to decide how many ships there will be")
    print("Closer to 0 means less ships, closer to 1 means more ships\n")
    difficulty = float(input("Please choose a number between 0 and 1: "))
    num_ships = difficulty * (board_dimension ** 2)
    return int(num_ships)

# A function that takes in the board and returns a random coord for a ship
# within the dimensions of that board
def find_new_ship(board):
    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board[0]) - 1)
    ship_location = [ship_row, ship_col]
    return ship_location

# A function that takes in the number of ships and the board_dimension
# and returns a list of randomly generated ships
def ship_list(no_ships, board):
    list_of_ships = []
    for ship in range(no_ships):
        ship_location = find_new_ship(board)
        # Makes sure there aren't multiple ships in same location
        while ship_location in list_of_ships:
            ship_location = find_new_ship(board)
        list_of_ships.append(ship_location)
    print(list_of_ships)
    return list_of_ships

def main():

    print_greeting()
    board_size = int(input("\nSize of board please: "))

    board = []
    for x in range(0, board_size):
        board.append(["O"] * board_size)

    print_board(board)

    ship_no = ship_num(board_size)
#    print(ship_no)

    shipems = ship_list(ship_no, board)

    guesses = []
    guess = get_guess(board_size)
    guesses.append(guess)

    guess_hit = check_hit(board, guesses, shipems, board_size)

    while guess_hit != True:
        would_continue()
        print("Your guesses thus far: ", guesses)
        print("The ship locations are: ", shipems)
        print
        guess_new = get_guess(board_size)
        while guess_new in guesses:
            print("\nYou guessed that one already.")
            print("Please guess again\n")
            guess_new = get_guess(board_size)
        guesses.append(guess_new)
        guess_hit = check_hit(board, guesses, shipems, board_size)

    print_board(board)
    print

main()

#@todo have checkhit check every ship in ship list to see if it is a hit

#@todo insert message to continue looking for ships after hitting the first

#@todo remove ships from ship list as they are hit
#@todo run program until ship list is empty
#   change condition for checkhit to return true when shiplist is empty.
#   then can keep same while loop

#@todo check that all inputs are proper and return input error to user when not
