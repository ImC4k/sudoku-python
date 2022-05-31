from copy import copy

boardSize = 9
emptyToken = 0
endDepth = boardSize * boardSize

def isRowValid(board, y, x, val):
    '''
    checks if val is a valid input in row y
    returns boolean
    '''
    pass

def isColumnValid(board, y, x, val):
    '''
    checks if val is a valid input in column x
    returns boolean
    '''
    pass

def getGroupIndex(i):
    '''
    (optional helper function to isAreaValid)
    returns a list of indices which i belongs with
    e.g. when i is 2, it should return [0, 1, 2]
    '''
    pass

def isAreaValid(board, y, x, val):
    '''
    checks if val is a valid input within its area
    returns boolean
    '''
    pass

def isCellValid(board, y, x, val):
    '''
    checks if val is a valid input across the entire board
    returns boolean
    '''
    pass


def printBoard(board):
    '''
    prints out the board
    should replace emptyToken with empty space ' ' for higher readability
    '''
    pass

def updateBoard(board, y, x, val):
    '''
    replace the specified slot on board with val
    (hint, here might need to use copy function imported builtin library)
    '''
    pass

def solveRecursive(board, depth):
    '''
    solve the sudoku problem recursively
    '''
    pass

def solve(board):
    '''
    entry point of the solver
    also print out the solution if found
    '''
    pass

board = [
    [4, 3, 0, 5, 0, 0, 0, 0, 6],
    [0, 0, 8, 0, 2, 0, 0, 1, 9],
    [0, 1, 7, 0, 0, 0, 4, 5, 0],
    [8, 6, 0, 2, 0, 0, 0, 7, 0],
    [0, 7, 4, 8, 0, 0, 2, 6, 0],
    [1, 0, 9, 0, 0, 7, 8, 3, 0],
    [2, 0, 0, 1, 7, 8, 0, 4, 3],
    [0, 0, 1, 9, 4, 0, 0, 0, 7],
    [0, 0, 0, 6, 5, 0, 0, 0, 0]
]

solve(board)

# # solution
# board = [
#     [4, 3, 2, 5, 1, 9, 7, 8, 6],
#     [6, 5, 8, 7, 2, 4, 3, 1, 9],
#     [9, 1, 7, 3, 8, 6, 4, 5, 2],
#     [8, 6, 5, 2, 3, 1, 9, 7, 4],
#     [3, 7, 4, 8, 9, 5, 2, 6, 1],
#     [1, 2, 9, 4, 6, 7, 8, 3, 5],
#     [2, 9, 6, 1, 7, 8, 5, 4, 3],
#     [5, 8, 1, 9, 4, 3, 6, 2, 7],
#     [7, 4, 3, 6, 5, 2, 1, 9, 8]
# ]