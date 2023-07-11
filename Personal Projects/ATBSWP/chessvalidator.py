def main():
    chessBoard = {
        "1h": "bking",
        "6c": "wqueen",
        "2g": "bbishop",
        "5h": "bqueen",
        "3e": "wking",
    }

    if isValidChessBoard(chessBoard) == True:
        print("Its a valid Chess Board.")
    else:
        print("Its NOT a valid Chess Board.")

    return


def isValidChessBoard(board):
    position = boardDefault()
    pieces = ["pawn", "knight", "bishop", "rook", "queen", "king"]

    # Checks if the players have each a maximun of 16 pieces.

    # Checks if the board has a maximun of 1 white and 1 black king.

    # Checks if the board has a maximun of 1 white and 1 black queen.

    # Checks if the board has a maximun of 2 white and 2 black knights, bishops and rooks.

    # Check if each of the players have a maximun of 8 pawns.

    # Check if the peaces are in valid position os the board.

    return True


def boardDefault():
    size = 8
    alfa = ["a", "b", "c", "d", "e", "f", "g", "h"]
    board = []

    for i in range(size):
        for j in alfa:
            place = str(i + 1) + j
            board.append(place)

    return board


main()
