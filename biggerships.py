class Ship(object):
    def __init__(self, coordinates, name = '', length = 1):
        self.length = length
        self.coordinates = coordinates
        self.name = name

def get_ship_name(ships_dict):
    key_name = input("""It's now time to name your ship. Please give it a unique name: """)
    if key_name in ships_dict:
        print("""You've already chosen that name for a ship.
            Each of your ships deserves a unique name.""")
        get_ship_name(ships_dict)
    return key_name

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

def get_end_point1(size_board):
    print("\nPlease give the row and column for the first endpoint of your ship\n")
    row = int(input("Row: "))
    column = int(input("Column: "))
    # If the guess is outside the dimension of the board, ask again
    while row not in range(1, size_board + 1) or \
        column not in range(1, size_board + 1):
        print("\nOops, that's not even in the ocean.")
        print("Please try again\n")
        row = int(input("Row: "))
        column = int(input("Column: "))

#    get_point = "\nPlease choose the end point for your ship: "
#    end_point1 = ship_from_user(board_dim, get_point)
    end_point1 = [row, column]
    return end_point1

def check_boundaries(point, size_board):
    if point[0] not in range(1, size_board + 1) or \
        point[1] not in range(1, size_board + 1):
        point = "%s, this option would not have been wihtin the boundaries of the board" % (point)
    return point

def present_options(e2a, e2b, e2c, e2d):
    #use dict instead of list
    #then can use the key as the name when printing options
    option_num = {}
#    option_num = []
    if type(e2a) is list:
#        option_num.append(e2a)
        option_num['a'] = e2a
    if type(e2b) is list:
#        option_num.append(e2b)
        option_num['b'] = e2b
    if type(e2c) is list:
#        option_num.append(e2c)
        option_num['c'] = e2c
    if type(e2d) is list:
#        option_num.append(e2d)
        option_num['d'] = e2d

    if len(option_num) != 4:
        print("""\nYour second end point can be 1 of 4 options.
Unfortunately, yours have been limited
Due to your choice of the first end point""")
        print("\nYour options are:\n")
        for point in option_num:
            print(point, " = ", option_num[point])

    if len(option_num) == 4:
        print("\nYour second end point can be 1 of 4 options.")
        for point in option_num:
            print(point, " = ", option_num[point])

#        print("Your options are a = %s, b = %s, c = %s, and d = %s") % (e2aS, e2bS, e2cS, e2dS)


def get_end_point2(e1, ship_length, size_board):
    e2a = [e1[0], e1[1] + ship_length - 1]
    e2b = [e1[0], e1[1] - ship_length + 1]
    e2c = [e1[0] + ship_length - 1, e1[1]]
    e2d = [e1[0] - ship_length + 1, e1[1]]

    e2a = check_boundaries(e2a, size_board)
    e2b = check_boundaries(e2b, size_board)
    e2c = check_boundaries(e2c, size_board)
    e2d = check_boundaries(e2d, size_board)

    #check if the options intersect other ships
    #exclude these if they are

    """
    if e2a[0] not in range(1, size_board + 1) or \
        e2a[1] not in range(1, size_board + 1):
        e2a = "%s, this option would not have been wihtin the boundaries of the board" % ([e1[0], e1[1] + ship_length])
    if e2b[0] not in range(1, size_board + 1) or \
        e2b[1] not in range(1, size_board + 1):
        e2b = "%s, this option would not have been wihtin the boundaries of the board" % ([e1[0], e1[1] - ship_length])
    if e2c[0] not in range(1, size_board + 1) or \
        e2c[1] not in range(1, size_board + 1):
        e2c = "%s, this option would not have been wihtin the boundaries of the board" % ([e1[0] + ship_length, e1[1]])
    if e2d[0] not in range(1, size_board + 1) or \
        e2d[1] not in range(1, size_board + 1):
        e2d = "%s, this option would not have been wihtin the boundaries of the board" % ([e1[0] - ship_length, e1[1]])

    e2aS = ', '.join(e2a)
    e2bS = ', '.join(e2b)
    e2cS = ', '.join(e2c)
    e2dS = ', '.join(e2d)
    """

#    print("Your second end point can be 1 of 4 options.")
#    print("Your options are a = %s, b = %s, c = %s, and d = %s") % (e2aS, e2bS, e2cS, e2dS)

    present_options(e2a, e2b, e2c, e2d)

    choice = False

    while choice == False:
        choice = input("""\nPlease choose which point you would like as your
second end point (enter 'a', 'b', 'c', 'd'): """)

        if choice == 'a':
            if type(e2a) is list: return e2a
            else:
                print("I told you this was not a valid choice")
                choice = False
        elif choice == 'b':
            if type(e2b) is list: return e2b
            else:
                print("I told you this was not a valid choice")
                choice = False
        elif choice == 'c':
            if type(e2c) is list: return e2c
            else:
                print("I told you this was not a valid choice")
                choice = False
        elif choice == 'd':
            if type(e2d) is list: return e2d
            else:
                print("I told you this was not a valid choice")
                choice = False
        else:
            print("That was not a valid choice. Please try again")
            choice = False


"""
# @todo change: make end point 2 a choice of 4 options based on length of ship
def get_end_point2.0(end_point1):
    print("\nPlease give the row and column for the second endpoint of your ship")
    row = int(input("Row: "))
    column = int(input("Column: "))
    end_point2 = [row, column]

    while end_point2 == end_point1:

        print("\nYou already chose this point as your first end point
Please choose the second end point such that it shares
Either a row or column (but not both) with the first end point")
        end_point2 = get_end_point2(end_point1)

    while end_point2[0] != end_point1[0] and end_point2[1] != end_point1[1]:
        print("\nThe ship must be placed either vertically or horizontally
Please choose the second end point such that it shares
Either a row or column (but not both) with the first end point")
        end_point2 = get_end_point2(end_point1)

    return end_point2

"""

def get_ship(ships_dict, ship_length, board_dim):
    lil_ship = []
    end_point1 = get_end_point1(board_dim)
    lil_ship.append(end_point1)
    end_point2 = get_end_point2(end_point1, ship_length, board_dim)
    lil_ship.append(end_point2)

    count = 1
    while ship_length != len(lil_ship):
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
        lil_ship.append(midpoint)

    for point in lil_ship:
        for key in ships_dict:
            for points in ships_dict[key]:
                while point == points:
                    print("""\nYour choice of end points has caused your ships to overlap.
Please try not to crash your ships into each other next time.
You will now be prompted to place a new ship.""")
                    get_ship(ships_dict, ship_length, board_dim)

    print("\nCongratulations! You have successfully chosen a location for your ship.")
    ship_name = get_ship_name(ships_dict)
    new_ship = Ship(lil_ship, ship_name, ship_length)
    ships_dict[ship_name] = lil_ship
    #ships_dict[ship_name] = new_ship.coordinates

def main():
    ships_dict = {}
    ship_length = 4
    board_size = 10

    for i in range(3):
        get_ship(ships_dict, ship_length, board_size)

    for key in ships_dict:
        print(key, ships_dict[key])

main()


def b():
    """
        for key in ships_dict:
            while end_point1 in ships_dict[key]:
                print("\nThere is a ship located there already.")
                print("Please choose another end point for your ship\n")
                end_point1 = ship_from_user(board_dim, get_point)
    """
