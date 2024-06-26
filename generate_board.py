import math
import random

#Create valid sudoku board
"""
Create three arrays: Rows, Columns, and 3x3's. Each array consists of 9 dictionaries each to account for each "sub-game" of 9 numbers.
Each of these dictionaries are keyed with numbers 1-9 mapped to a boolean value.
Initially, all values are considered false until we place a number into the board.
When this happens, we need to update all three of the dictionaries it belongs to.
This is because any given number on the board corresponds to three sub-games: It needs to be unique in its row, column, and 3x3 subgrid.
We can call the 3x3 subgrids "squares" for sake of simplicity
We can use truth statements to get a pool of candidate numbers and then randomly select one to place. Repeat this process until board is full.
"""

def create_dicts():
    Rows = []
    Cols = []
    Squares = []

    for i in range(9):
        Rows.append({i: False for i in range(1, 10)})
        Cols.append({i: False for i in range(1, 10)})
        Squares.append({i: False for i in range(1, 10)})

    return [Rows, Cols, Squares]

"""
When we index, the first index is the number column, row, or square we want. The second index is accessing a dictionary value using the number key
        Cols[1][4] = True ==> Takes the second column (indexing starts from 0 since this is a list) and accesses the value associated with the number 4
        Rows[2][3] = True ==> We're grabbing the third row and setting the bool associated with key number 3 to True
        Rows[0][1] is the very first element. 
"""
# Rows[0][1] = True
# print(Rows)

# Create empty 9x9 game board


"""
for i in range(100):
    print(random.randint(1,9))  Both bounds are inclusive
"""

def get_square(i,j):
    subgrid_row = i // 3
    subgrid_col = j // 3
    
    subgrid_number = subgrid_row * 3 + subgrid_col + 1
    
    return subgrid_number - 1

def ran_num(length):
    return random.randint(1,length) - 1

# Iterate over every coordinate
def get_valid_number(i, j, Rows, Cols, Squares):
    unused_row_nums = set([key for key, value in Rows[i].items() if value == False])
    unused_col_nums = set([key for key, value in Cols[j].items() if value == False])
    unused_square_nums = set([key for key, value in Squares[get_square(i,j)].items() if value == False])

    intersection_list = list(unused_row_nums & unused_col_nums & unused_square_nums)
    if len(intersection_list) == 0:
        return 99
    
    return intersection_list[ran_num(len(intersection_list))]

def update_dicts(i, j, val, Rows, Cols, Squares):    
    Rows[i][val] = True
    Cols[j][val] = True
    Squares[get_square(i,j)][val] = True

def print_board(board):
    # for row in board[:-1]:
    #     print (row) 
    # print(board[-1])
    for row in board:
        print(row)   

def print_board_object(board_object):
    print_board(board_object[0])
    print('Attempts:', str(board_object[1]), '\n')


def populate_board():
    dicts = create_dicts()
    Rows = dicts[0]
    Cols = dicts[1]
    Squares = dicts[2]
    board = []
    for i in range(9):
        board.append([0 for i in range(9)])

    for i in range(9):
        for j in range(9):
            num = get_valid_number(i, j, Rows, Cols, Squares)
            if num == 99: return [False, 0]
            
            board[i][j] = num
            update_dicts(i, j, num, Rows, Cols, Squares)
        
    return [True, board]      

# Return a list where: First element is the generated sudoku board and Second element is the number of attempts for generation
def create_board():
    valid_board = [False, 0]
    attempt_count = 0

    while valid_board[0] == False:
        valid_board = populate_board()
        attempt_count += 1

    # print_board(valid_board[1])
    # print('Attempt number: ', str(attempt_count)) 
    return [valid_board[1], attempt_count]


