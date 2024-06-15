import numpy as np

""" First of all, I have conceived many attempts to build this mini-game, before succeeding.
Also I followed during my code in place journey learnings on: codecademy.com (The introduction to python3), some Programming Hub courses
Harvard CS50 and the beginning of Harvard CS50 AI.Which is why I use sometimes some coding schedules which were not teached in code in place courses.
I had several original ideas for my project but unfortunately I have not yet enough skills to design them, at this time.
Unlike many Tic-tac-Toe games made during past years, I wanted to do something more tricky
and a bit more ambitious with this Connect4 game.
"""
# Dimensions of the grid, it is a common 7x6, connect4 grid
columns = 7
rows = 6

# Let's use numpy to create the grid of the game
grid = np.zeros((rows, columns))

# Dimensions of the grid, it is a common 7x6, connect4 grid
columns = 7
rows = 6

# The following function will status on the grid game at every moment
def show_grid(grid):
    for row in grid:
        print(' '.join(map(str, map(int, row))))
    print(" ")

# This is the function where a token is placed in the grid
def put_token(grid, column, player):
    for row in range(rows-1, -1, -1):
        if grid[row][column] == 0:
            grid[row][column] = player
            return True
    return False

# Function for checking if someone won and which will be applied every turn
def winning(grid, player):
    # check if there is an horizontal winning
    for row in range(rows):
        for col in range(columns - 3):
            if all([grid[row][col + i] == player for i in range(4)]):
                return True

    # check if there is a vertical winning
    for col in range(columns):
        for row in range(rows - 3):
            if all([grid[row + i][col] == player for i in range(4)]):
                return True

    # Check slope winning
    for row in range(rows - 3):
        for col in range(columns - 3):
            if all([grid[row + i][col + i] == player for i in range(4)]):
                return True

    for row in range(3, rows):
        for col in range(columns - 3):
            if all([grid[row - i][col + i] == player for i in range(4)]):
                return True

    return False


show_grid(grid)


turn = 0
#Playing each turn until someone win with a while boucle
while True:
    # Player 1 Turn
    if turn == 0:
        x = int(input("Player 1, select a column (0-6): "))
        if 0 <= x < columns:
            if put_token(grid, x, 1):
                if winning(grid, 1):
                    print("Player 1 won!")
                    break
                turn = 1
            else:
                print("Column is full. Choose another one.")
        else:
            print("Invalid column. Choose a number between 0 and 6.")
    else:
        x = int(input("Player 2, select a column (0-6): "))
        if 0 <= x < columns:
            if put_token(grid, x, 2):
                if winning(grid, 2):
                    print("Player 2 won!")
                    break
                turn = 0
            else:
                print("Column is full. Choose another one.")
        else:
            print("Invalid column. Choose a number between 0 and 6.")

    # Show the grid
    show_grid(grid)
