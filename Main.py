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
        x = int(input("Enter X:\t"))
        y = int(input("Enter y:\t"))
        gameOver = board.RevealTiles(x, y)
    print(board)

if __name__ == "__main__":
    main()