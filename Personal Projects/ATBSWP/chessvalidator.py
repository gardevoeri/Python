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

    # Check if the peaces are in valid positions on the board.
    for k in board.keys():
        if k not in position:
            print("The peaces position are not in a valid board!")
            return False

    # Checks if the board has only black or white pieces.
    for i in board.values():
        if i[0] == "b":
            if i[1:] not in pieces:
                print("Invalid black pieces in the board!")
                return False
        elif i[0] == "w":
            if i[1:] not in pieces:
                print("Invalid white pieces in the board!")
                return False
        else:
            print("Invalid pieces in the board!")
            return False

    # Checks if the board has a maximun number of each of the pieces.
    piecesOnBoard = {}
    for piece in pieces:
        for value in board.values():
            if value[1:] == piece:
                if value in piecesOnBoard.keys():
                    piecesOnBoard[value] += 1
                else:
                    piecesOnBoard[value] = 1

    for k, v in piecesOnBoard.items():
        if k[1:] == "pawn":
            if v > 8:
                print("Invalid number of pawns on the board")
                return False
        elif k[1:] == "knight":
            if v > 2:
                print("Invalid number of knights on the board")
                return False
        elif k[1:] == "bishop":
            if v > 2:
                print("Invalid number of bishop on the board")
                return False
        elif k[1:] == "rook":
            if v > 2:
                print("Invalid number of rook on the board")
                return False
        elif k[1:] == "king":
            if v > 1:
                print("Invalid number of kings on the board")
                return False
        elif k[1:] == "queen":
            if v > 1:
                print("Invalid number of queens on the board")
                return False

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
