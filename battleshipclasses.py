# according to total ship numbers, 44% of 10x10 has a ship in a space
# filled_spaces = 0.44 * (board_size ** 2)
44% of spots should be occupied

class Ship(object):
    def __init__(self, coordinates, name = '', length = 1):
        self.length = length
        self.coordinates = coordinates
        self.name = name

class Carrier(Ship):
    length = 5
    # 1 carrier in 10x10
    total_ships = 1
    # for player to choose
    # total_ships = int(input("How many carriers would you like there to be?"))

class Battleship(Ship):
    length = 4
    total_ships = 2

class Cruiser(Ship):
    length = 3
    total_ships = 3

class Submarine(Ship):
    length = 3
    total_ships = 4

class Destroyer(Ship):
    length = 2
    total_ships = 5

class Player(object):
    # name is the name of the ship, shoudl be a string
    # ships_dict is the dictionary of ship locations
    # guessing_board will be the board where they keep track of their player's own guesses
    # tracking_board will be the board where they keep track of opponents guesses
    def __init__(self, name, ships_dict, guessing_board, tracking_board):
        self.name = name
        self.ships_dict = ships_dict
        self.guessing_board = guessing_board
        self.tracking_board = tracking_board

class Board(object):
    def __init__(self, board_size = 10, ships_dict):
        self.board_size = board_size
        self.ships_dict = ships_dict



ships_dict = {}
"""
ships = {}
ships['a'] = [[1,2],[3,4]]
ships['b'] = [[3,4], [9,6]]
print(ships)
for key in ships:
  while point in ships[key]:
"""


def get_ship(ships_dict, ship_length, board_dim):
    ship = []
    get_point = "\nPlease choose the end point for your ship: "
    end_point1 = ship_from_user(board_dim, get_point)
    for key in ships_dict:
        while end_point1 in ships_dict[key]:
            print("\nThere is a ship located there already.")
            print("Please choose another end point for your ship\n")
            end_point1 = ship_from_user(board_dim, get_point)

    ship.append(end_point1)

    get_point2 = "\nPlease choose the second end point for your ship: "
    end_point2 = ship_from_user(board_dim, get_point2)
    while end_point2 == end_point1:
        print("\nYou already chose this point as your first end point")
        print("Please choose the second end point such that it shares")
        print("Either a row or column (but not both) with the first end point")
        end_point2 = ship_from_user(board_dim, get_point)

    while end_point2[0] != end_point1[0] and end_point2[1] != end_point1[1]:
        print("""\nThe ship must be placed either vertically or horizontally
            Please choose the second end point such that it shares
            Either a row or column (but not both) with the first end point""")
        end_point2 = ship_from_user(board_dim, get_point)

    ship.append(end_point2)

    while ship_length != len(ship):
        count = 1
        # find mid points
        # first determine if ship is vertical or horizontal
        # make new ship points between the end points using a loop and append to ship list

        #or import math and find some doodad that gives you the points between 2 end points
        if end_point2[0] == end_point1[0] and end_point2[1] > end_point1[1]:
            midpoint = [end_point2[0], end_point2[1] - count]
        elif end_point2[0] == end_point1[0] and end_point2[1] < end_point1[1]:
            midpoint = [end_point2[0], end_point2[1] + count]
        elif end_point2[1] == end_point1[1] and end_point2[0] > end_point1[0]:
            midpoint = [end_point2[0] - count, end_point2[1]]
        elif end_point2[1] == end_point1[1] and end_point2[0] < end_point1[0]:
            midpoint = [end_point2[0] + count, end_point2[1]]
        count += 1
        ship.append(midpoint)

    for point in ship:
        for key in ships_dict:
            for points in ships_dict[key]:
                if point == points:
                    print("""\nYour choice of end points has caused your ships to overlap.
                        Please try not to crash your ships into each other next time.
                        You will now be prompted to place a new ship.""")
                    get_ship(ships_dict, ship_length, board_dim)

    print("\nCongratulations! You have successfully chosen a location for your ship.")
    ship_name = get_ship_name(ships_dict)
    new_ship = Ship(ship, ship_name, ship_length)
    ships_dict[ship_name] = new_ship

def get_ship_name(ships_dict):
    key_name = input("""It's now time to name your ship. Please give it a unique name: """)
    if key_name in ships_dict:
        print("""You've already chosen that name for a ship.
            Each of your ships deserves a unique name.""")
        get_ship_name(ships_dict)
    return key_name

#ask the board where the ship is on it
#have the board store ship locations

def get_player_ships(ship_no, board_size):
    player_ships = []
    place_ship = "\nPlease choose the end point for a ship: "
    for ship in range(ship_no):
#        print("Please choose the location for a ship: ")
        ship_end = ship_from_user(board_size, place_ship)
        while ship_end in player_ships:
            print("\nThere is a ship located there already.")
            print("Please place another ship\n")
            ship_end = ship_from_user(board_size, place_ship)
        player_ships.append(ship_end)
    print("\nHere is your list of secretly located ships: ", player_ships)
    return player_ships

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
