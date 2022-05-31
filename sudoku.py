from copy import copy

boardSize = 9
emptyToken = 0
endDepth = boardSize * boardSize

def isRowValid(board, y, x, val):
    row = board[y]
    return val not in row

def isColumnValid(board, y, x, val):
    column = [row[x] for row in board]
    return val not in column

def getGroupIndex(i):
    if i < 3:
        return [0, 1, 2]
    elif i < 6:
        return [3, 4, 5]
    else:
        return [6, 7, 8]

def isAreaValid(board, y, x, val):
    yGroup = getGroupIndex(y)
    xGroup = getGroupIndex(x)
    for i in yGroup:
        for j in xGroup:
            if board[i][j] == val:
                return False
    return True

def isCellValid(board, y, x, val):
    return isRowValid(board, y, x, val) and isColumnValid(board, y, x, val) and isAreaValid(board, y, x, val)


def printBoard(board):
    for row in board:
        replaceEmpty = [str(val) if val != emptyToken else ' ' for val in row]
        print(' '.join(replaceEmpty))

def updateBoard(board, y, x, val):
    updatedBoard = copy(board)
    updatedBoard[y][x] = val
    return updatedBoard

def solveRecursive(board, depth):
    if depth == endDepth:
        return board
        
    y = depth // boardSize
    x = depth % boardSize

    if board[y][x] != emptyToken: # provided value, must be correct
        return copy(solveRecursive(board, depth + 1))

    for val in range(1, boardSize + 1):
        if isCellValid(board, y, x, val):
            updatedBoard = updateBoard(board, y, x, val) # replace slot with value, assume it's correct
            deepBoardResult = copy(solveRecursive(updatedBoard, depth + 1))
            if deepBoardResult is not None:
                return deepBoardResult
        updatedBoard = updateBoard(board, y, x, 0) # revert update, required because python is dumb (it created updatedBoard variable in function scope)
    return None # no value is valid for this cell, must have some problem previously, back track

def solve(board):
    solvedBoard = solveRecursive(board, 0)

    if solvedBoard is None:
        print('no solution for this board')
    else:
        print('found solution: ')
        printBoard(solvedBoard)

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