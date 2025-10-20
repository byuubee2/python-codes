def isValidChessboard(board):


chessBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
isValidChessboard(chessBoard)

###checklist:
   # check if the keys in the dictionary are valid squares
    #check the total number of pieces of white or black exceeds 16
   # check if the total number of pawns of each color exceeds 8
   # check if black or white has exactly 1 king

