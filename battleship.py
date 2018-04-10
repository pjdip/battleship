from random import randint
from pprint import pprint
import sys

# Let's the user know what this jam is all about
def print_greeting():
    print("\nWelcome, this is a game of battleship.")
    print("You will first decide the size of the board")
    print("The board will be square, you choose the dimension")

# A function that takes in the board as an argument and prints it
def print_board(board):
    print("\nHere is your board:\n")
    # Prints the column header
    for col in range(len(board) + 1):
        # Built-in print function has end='\n' and sep='' parameters
        # 'End' allows us to change the char a printed line ends with
        print(col, end = " ")
    print()
    row_count = 1
    for row in board:
        print(row_count, " ".join(row))
        row_count += 1
    print()

# A function that takes in the dimension of the board
# and returns the users guess of ship location
# prompts the user for a guess as to location of ships
def ship_from_user(size_board, directions):
    print(directions)
    guess_row = int(input("Row: "))
    guess_col = int(input("Col: "))
    # If the guess is outside the dimension of the board, ask again
    while guess_row not in range(1, size_board + 1) or \
        guess_col not in range(1, size_board + 1):
        print("\nOops, that's not even in the ocean.")
        print("Please try again\n")
        guess_row = int(input("Row: "))
        guess_col = int(input("Col: "))
    else:
        return [guess_row, guess_col]

# A function that takes in 4 arguments
# 1) the board itself 2) a list containing all coordinates that have been guessed
# 3) a list containing all ship coordinates 4) board dimension
# Checks if a guess is at the same coord as a ship
# Returns true if all ships are sunk
# Alters the board for hits and misses
# Removes ships from list of ships as they are hit
def check_hit(board, list_guesses, list_ships, size_board, player):
    # Checking the most recent guess, or last guess in guess list
    guess = list_guesses[-1]
    row_guess, col_guess = guess[0] - 1, guess[1] - 1

    if player == True:
        # If the guess shares a location with a ship
        if guess in list_ships:
            # Remove the ship from the list of ships
            list_ships.remove(guess)
            # If there are no more ships
            if list_ships == []:
                print("\nCongratulations! You sank all enemy ships! :P\n")
                print("Isn't victory sweet?\n")
                board[row_guess][col_guess] = "X"
                return True
                sys.exit()
            else:
                print("\nCongratulations! You sank an enemy ship!\n")
                board[row_guess][col_guess] = "X"
        else:
            board[row_guess][col_guess] = "-"
            print("\nYou missed my battleship!")
            #print("Please guess again\n")
#        print_board(board)

    else:
        if guess in list_ships:
            list_ships.remove(guess)
            if list_ships == []:
                board[row_guess][col_guess] = "X"
                return True
            else:
                board[row_guess][col_guess] = "X"
                print("The computer hit one of your ships! D:")
        else:
            board[row_guess][col_guess] = "-"

    print
#    return board

# A function that checks if the user wants to keep playing
def would_quit():
    to_continue = input("Would you like to continue? respond Y or N: ")
    if to_continue == "N" or to_continue == "n":
        return True

# A function that takes in the size of the board as an arguments
# Asks user if they want there to be a lot of ships
# Returns the number of ships
#@todo could just ask user how many ships they want
def ship_num(board_dimension):
    print("You will now choose a difficulty for the game")
    print("Pick a decimal between 0 - 1 to decide how many ships there will be")
    print("Closer to 0 means less ships, closer to 1 means more ships\n")
    difficulty = float(input("Please choose a number between 0 and 1: "))
    num_ships = difficulty * (board_dimension ** 2)
    return int(num_ships)

# A function that takes in the board and returns a random coord for a ship
# within the dimensions of that board
def find_rand_ship(board):
    ship_row = randint(1, len(board))
    ship_col = randint(1, len(board[0]))
    ship_location = [ship_row, ship_col]
    return ship_location

# A function that takes in the number of ships and the board_dimension
# and returns a list of randomly generated ships
def ship_list(no_ships, board):
    list_of_ships = []
    for ship in range(no_ships):
        ship_location = find_rand_ship(board)
        # Makes sure there aren't multiple ships in same location
        while ship_location in list_of_ships:
            ship_location = find_rand_ship(board)
        list_of_ships.append(ship_location)
    #print("this is the list of ships", list_of_ships)
    return list_of_ships

def get_player_ships(ship_no, board_size):
    player_ships = []
    place_ship = "\nPlease choose the location for a ship: "
    for ship in range(ship_no):
#        print("Please choose the location for a ship: ")
        ship_loc = ship_from_user(board_size, place_ship)
        while ship_loc in player_ships:
            print("\nThere is a ship located there already.")
            print("Please place another ship\n")
            ship_loc = ship_from_user(board_size, place_ship)
        player_ships.append(ship_loc)
    print("\nHere is your list of secret ships: ", player_ships)
    return player_ships

def player_status(ships, guesses, board):
    print("\nYour guesses thus far: ", guesses)
    print("Your remaining ship locations are: ", ships)
    print("Your board state looks as follows:")
    print_board(board)
    print("""\n'-' represents a location you have guessed that was a miss
'x' represents a location you have guessed that was a hit
'O' represents a location you have not yet guessed\n""")


def player_check(player, passcode):
    print("\nIt is now %s's turn" % (player))
    pass_input = input("Please input the passcode for %s: " % (player))
    while pass_input != passcode:
        pass_input = input("\nThat passcode was incorrect, please try again: ")
    print("\n\nWelcome to your turn %s" % (player))
    return True

def previous_guess(guess, guess_list, board_size):
    guess_ship = "\nPlease guess the location of an enemy ship: "
    while guess in guess_list:
        print("""\nYou guessed that one already
Please guess again\n""")
        guess = ship_from_user(board_size, guess_ship)
    return guess

def main():

    print_greeting()
    board_size = int(input("\nPlease decide the dimension of board: "))
# for n players ask number of players and then do for loop creating player object for each person
    player_1 = input("\nPlease enter the name of the first player: ")
    passcode_1 = input("Please enter a code you will use when passing turns: ")
    player_2 = input("\nPlease enter the name of the second player: ")
    passcode_2 = input("Please enter a code you will use when passing turns: ")

#    board_size = 10
    player1_board = []
    player2_board = []
    for x in range(0, board_size):
        player1_board.append(["O"] * board_size)
        player2_board.append(["O"] * board_size)

    guess_ship = "\nPlease guess the location of an enemy ship: "
#    guess2_ship = "\nThe second player will now guess the location of an enemy ship: "

#    print_board(board)
#    print_board(cpu_board)

    print("\nYour board is", board_size, "x", board_size)
    print("There are", board_size ** 2, "available spaces for ships.")
    ship_no = int(input("How many ships would you like?: "))
#    ship_no = ship_num(board_size)
#    print(ship_no)

#    shipems = ship_list(ship_no, board)
#    player_check(passcode_1)
    player_check(player_1, passcode_1)
    print("You will now choose the location for their ships")
    player1_shipems = get_player_ships(ship_no, board_size)

    player_check(player_2, passcode_2)
    print("You will now choose the location for their ships")
    player2_shipems = get_player_ships(ship_no, board_size)

    player_check(player_1, passcode_1)
    player1_guesses = []
    player1_guess = ship_from_user(board_size, guess_ship)
    player1_guesses.append(player1_guess)
    guess1_hit = check_hit(player1_board, player1_guesses, player2_shipems, board_size, True)

    player_check(player_2, passcode_2)
    player2_guesses = []
    player2_guess = ship_from_user(board_size, guess_ship)
    player2_guesses.append(player2_guess)
    guess2_hit = check_hit(player2_board, player2_guesses, player1_shipems, board_size, True)

#    guess_hit = check_hit(board, guesses, shipems, board_size, True)

    while guess1_hit != True and guess2_hit != True:

        """
        if guess_hit_cpu == True:
            print("\nGAME OVER\n")
            print("The computer sank all of your ships\n")
            print_board(cpu_board)
            print("The CPU guess were: ", cpu_guesses)
            print("The remaining CPU ship locations are: ", cpu_shipems)
            print

            sys.exit()


        if would_quit() == True:
            sys.exit()
        """

        player_check(player_1, passcode_1)
        player_status(player1_shipems, player1_guesses, player1_board)
        new_guess1 = ship_from_user(board_size, guess_ship)
        guess1_new = previous_guess(new_guess1, player1_guesses, board_size)
        player1_guesses.append(guess1_new)
        guess1_hit = check_hit(player1_board, player1_guesses, player2_shipems, board_size, True)

        """
        guess1_new = ship_from_user(board_size, guess_ship)
        while guess1_new in player1_guesses:
            print("\nYou guessed that one already.")
            print("Please guess again\n")
            guess1_new = ship_from_user(board_size, guess_ship)
        """

        player_check(player_2, passcode_2)
        player_status(player2_shipems, player2_guesses, player2_board)
        new_guess2 = ship_from_user(board_size, guess_ship)
        guess2_new = previous_guess(new_guess2, player2_guesses, board_size)

        player2_guesses.append(guess2_new)
        guess2_hit = check_hit(player2_board, player2_guesses, player1_shipems, board_size, True)


#    print_board(board)
#    print_board(cpu_board)
    print

main()

#@todo have checkhit check every ship in ship list to see if it is a hit

#@todo insert message to continue looking for ships after hitting the first

#@todo remove ships from ship list as they are hit
#@todo run program until ship list is empty
#   change condition for checkhit to return true when shiplist is empty.
#   then can keep same while loop

#@todo check that all inputs are proper and return input error to user when not

#@todo silly easter egg: for board size n or greater, randomly generate "buried treasure"
