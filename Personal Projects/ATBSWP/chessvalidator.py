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
    position = [
        ["1a", "2a", "3a", "4a", "5a", "6a", "7a", "8a"],
        ["1b", "2b", "3b", "4b", "5b", "6b", "7b", "8b"],
        ["1c", "2c", "3c", "4c", "5c", "6c", "7c", "8c"],
        ["1d", "2d", "3d", "4d", "5d", "6d", "7d", "8d"],
        ["1e", "2e", "3e", "4e", "5e", "6e", "7e", "8e"],
        ["1f", "2f", "3f", "4f", "5f", "6f", "7f", "8f"],
        ["1g", "2g", "3g", "4g", "5g", "6g", "7g", "8g"],
        ["1h", "2h", "3h", "4h", "5h", "6h", "7h", "8h"],
    ]

    pieces = ["pawn", "knight", "bishop", "rook", "queen", "king"]

    # Checks if the players have each a maximun of 16 pieces.

    # Checks if the board has a maximun of 1 white and 1 black king.

    # Checks if the board has a maximun of 1 white and 1 black queen.

    # Checks if the board has a maximun of 2 white and 2 black knights, bishops and rooks.

    # Check if each of the players have a maximun of 8 pawns.

    # Check if the peaces are in valid position os the board.

    return True


main()
