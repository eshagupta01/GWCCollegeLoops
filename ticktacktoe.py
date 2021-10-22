#tick tack toe

import numpy as np

def printBoard(board, size):
    for row in range(size):
        for col in range(size):
            print (board[row][col], end = '')
        print()
    

def takeTurn(board, row, col, symbol):
    if symbol == 0:
        board[row][col] = 'O '
    else:
        board[row][col] = 'X '

def checkVertical(board, size):
    new_board = np.transpose(board)
    for row in range(size):
        matching = True
        prev = None
        for col in range(size):
            if prev == None:
                if new_board[row][col] == 'X ' or new_board[row][col] == 'O ':
                    prev = new_board[row][col]
                else:
                    matching = False
                    break

            elif prev != new_board[row][col] or new_board[row][col] == '* ':
                matching = False
                break
        if matching:
            return True
    return False


def checkHorizontal(board, size):
    for row in range(size):
        matching = True
        prev = None
        for col in range(size):
            if prev == None:
                if board[row][col] == 'X ' or board[row][col] == 'O ':
                    prev = board[row][col]
                   
                else:
                    matching = False
                    break
                    
            elif prev != board[row][col] or board[row][col] == '* ':
                matching = False
                break 
        if matching: return True
    return False

def checkLeftToRightDiagonal(board, size):
    prev = None
    for i in range(size):
        if prev == None:
            if board[i][i] == 'X ' or board[i][i] == 'O ':
                prev = board[i][i]
            else:
                return False

        elif board[i][i] != prev or board[i][i] == '* ':
            return False
    return True

def checkRightToLeftDiagonal(board, size):
   
    row = 0
    col = 2
    prev = None
    while(row <= 2 and col >= 0):
        if prev == None:
            if board[row][col] == 'X ' or board[row][col] == 'O ':
                prev = board[row][col]
            else:
                return False

        elif board[row][col] != prev or board[row][col] == '* ':
            return False
        row += 1
        col -= 1
    return True

if __name__ == '__main__':

    #game setup
    size = 3 #board size
    board = [['* ', '* ', '* '], ['* ', '* ', '* '], ['* ', '* ', '* ']] #board array
    print('Welcome to tick tack toe') #indicate to the user that the game started
    symbol = 0 #determines if the symbol is O or X

    #play game
    while(True):

        print('Enter the row followed by a space followed by the column number')
        turn = input().split()
        for i in range(len(turn)):
            turn[i] = int(turn[i])
        takeTurn(board,turn[0],turn[1],symbol)
        printBoard(board, size)
        print()


        if checkHorizontal(board, size):
            break
        if checkLeftToRightDiagonal(board,size): 
            break
        if checkRightToLeftDiagonal(board,size): 
            break
        if checkVertical(board, size):
            break

    
        symbol = not symbol

    #End Game
    print('Game Over')
    printBoard(board, size)






    
        
