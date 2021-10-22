#tic tac toe

def printBoard(board, size):

   

def takeTurn(board, row, col, symbol):
    if symbol == 0:
        board[row][col] = 'O '
    else:
        board[row][col] = 'X '



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
    prev = None
    for i in range(size-1, -1, -1):
        if prev == None:
            if board[i][i] == 'X ' or board[i][i] == 'O ':
                prev = board[i][i]
            else:
                return False

        elif board[i][i] != prev or board[i][i] == '* ':
            return False
    return True

if __name__ == '__main__':

    ########################### GAME SET UP CODE STARTS ###################################
    
    symbol = 0 #determines if the symbol is O or X

    




    ########################### GAME SET UP CODE ENDS ###################################
    





    ########################### PLAY GAME CODE STARTS ###################################
   
        
    symbol = not symbol
    

    ########################### PLAY GAME CODE ENDS ####################################







    ########################### END GAME CODE STARTS ####################################
    






    ########################### END GAME CODE ENDS ####################################






    
        
