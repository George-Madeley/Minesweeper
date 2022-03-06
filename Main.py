from Board import Board

def main():
    """Runs minesweeper."""
    width = int(input("Enter Width:\t"))
    height = int(input("Enter Height:\t"))
    maxBombs = int(input("Enter Bombs:\t"))
    board = Board(width, height, maxBombs)
    gameOver = False
    while not gameOver:
        print(board)
        placeFlag = str(input("Place flag (Y/N):\t")).lower() == "y"
        x = int(input("Enter X:\t"))
        y = int(input("Enter y:\t"))
        if placeFlag:
            board.PlaceFlag(x, y)
            gameOver = board.AreAllBombsFound()
        else:
            gameOver = board.RevealTiles(x, y) or board.AreAllBombsFound()
    print(board)

if __name__ == "__main__":
    main()