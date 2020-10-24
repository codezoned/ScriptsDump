""" 
    Author : Mohit Kumar

    9*9 Sudoku Solver in python using Backtracking 
    
    Given a partially filled 9×9 2D array, the objective is to fill a 9×9
    square grid with digits numbered 1 to 9, so that every row, column, and
    and each of the nine 3×3 sub-grids contains all of the digits.

    In This Solver we try filling digits one by one. Whenever we find that current 
    digit cannot lead to a solution, we remove it (backtrack) and try next digit. 
    This is better than naive approach (generating all possible combinations of digits
    and then trying every combination one by one as it drops a set of permutations
    whenever it backtracks.


"""
from typing import List, Tuple

Table = List[List[int]]  # typing hint for board

# intial values of sudoku board
# 0 represents place to be filled

board = [
    [5, 0, 0, 0, 0, 0, 0, 0, 0],
    [3, 4, 0, 1, 0, 0, 0, 0, 7],
    [0, 9, 0, 0, 0, 6, 0, 0, 0],
    [6, 0, 0, 0, 2, 0, 0, 0, 9],
    [0, 0, 4, 9, 8, 0, 1, 0, 0],
    [0, 1, 0, 0, 4, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 2, 6],
    [0, 0, 0, 0, 0, 0, 8, 0, 0],
    [9, 0, 0, 0, 0, 0, 3, 4, 0],
]


def find_empty(board: Table) -> Tuple[int, int]:
    """
    This function finds the empty position
    to be filled

    Parameters :
        Input : Sudoku Table
        Output : Tuple[int,int]
                 value of row and column of empty position

    """
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == 0:
                return (i, j)


def valid(board: Table, num: int, pos: Tuple[int, int]) -> bool:
    """
    This function checks the Table to see if each row,
    column, and the 3x3 subgrids contain the digit 'num.
    It returns False if it is not 'safe' (a duplicate digit
    is found) else returns True if it is 'safe'

    Parameters :
    Input : Board : Table
            num : int
            pos : Tuple[int, int]
                  which contain(row, column) of pos
    """

    for i in range(len(board)):
        # this loop checks number in same row and column
        if board[pos[0]][i] == num or board[i][pos[1]] == num:
            return False

    # these are the row and column value for 3*3 subgrid
    # in which the num belong
    cur_row = 3 * (pos[0] // 3)
    cur_col = 3 * (pos[1] // 3)

    # this loop check for the num present in 3*3 subgrid
    for i in range(cur_row, cur_row + 3):
        for j in range(cur_col, cur_col + 3):
            if board[i][j] == num:
                return False
    return True


def solve(board: Table) -> bool:
    """
    This is Solver function which uses Backtracking
    it repeatedly fills values in empty spaces and if filled
    value is wrong it backtracks to last value and start filling again
    with diffrent value

    Parameteres :
    Input : Board : Table

    Output : True if it solves the Sudoku Table
             False if Sudoku Table is incorrect

    """
    # finds the empty position to be filled
    find = find_empty(board)

    if not find:

        # if no empty position is there
        # we solved sudoku and returns True
        return True
    else:
        # row and column value for the corresponding empty position
        row, col = find

    # this loop fills the value from 1- 10 to empty position
    for i in range(1, 10):

        # this checks if corresponding filled value is correct or not
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                # if value is correct then moves to next value
                return True

            # if value is not correct mark this as empty
            board[row][col] = 0

    # backtracks to previous filled value
    return False


def print_board(board: Table) -> None:
    """
    This function prints Board  in form of
    9*9 matrix
    """
    for i in range(len(board)):
        if i % 3 == 0 and i > 0:
            print("- - - - - - - - - - - - - - -  ")
        for j in range(len(board[i])):
            if j % 3 == 0 and j > 0:
                print("| ", end="")
            print(board[i][j], " ", end="")
            if j == len(board[i]) - 1:
                print("\n")


print("Before Solving Sudoku : \n")
print_board(board)
if solve(board):
    print("\n********After Solving *********\n")
    print_board(board)
else:
    print("Enter Valid 3*3 sudoku pattern\n")
