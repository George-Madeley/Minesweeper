from random import randint
from re import L
from Tile import Tile


class Board:
    def __init__(self, sizeX: int, sizeY: int, maxBombs: int) -> None:
        self.__2DTileArray = [[Tile() for x in range(sizeX)] for y in range(sizeY)]
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.GenerateBombs(maxBombs)

    def __str__(self) -> str:
        """
        Foramts the string representation of the board and returns it.
        """

        boardString = ""
        for index, tileArray in enumerate(self.__2DTileArray):
            boardString += f"str(index)\t"
            for tile in  tileArray:
                boardString += str(f" {str(tile)} ")
            boardString += "\n"
        return boardString


    def GenerateBombs(self, maxBombs: int) -> None:
        """
        Generates a given amount of bombs and places them onto the board.

        Args:
            maxBombs: The number of bombs to be placed onto the board.
        """

        bombsGenerated = int(maxBombs)
        while bombsGenerated > 0:
            x = randint(self.__sizeX)
            y = randint(self.__sizeY)
            try:
                bombTile: Tile = self.__2DTileArray[y][x]
                if bombTile.IsBomb():
                    continue
                bombTile.SetBomb()
                self.IncrementSurroundingTiles(x, y)
                bombsGenerated -= 1
            except IndexError:
                pass

    def IncrementSurroundingTiles(self, x: int, y: int) -> None:
        """
        Increments the surrounding tiles of a bomb by one.

        Args:
            x: The X-coordinate of a bomb.
            y: The Y-coordinate of a bomb.
        """

        for innerY in range(y - 1, y + 2):
            for innerX in range(x - 1, x + 2):
                if innerX == x and innerY == y:
                    continue
                try:
                    surroundingTile: Tile = self.__2DTileArray[innerY][innerX]
                    surroundingTile.IncrementNumber()
                except IndexError:
                    pass

    def RevealTiles(self, x: int, y: int) -> bool:
        """
        Reveals selected and any other tiles.
        
        Args:
            x: The X-coordinate of the selected tile.
            y: The Y-coordinate of the selected tile.

        Returns:
            True if the tile was a bomb.
        """

        selectedTile: Tile = self.__2DTileArray[y][x]
        selectedTile.SetExplored()
        if selectedTile.IsBomb():
            return True
        elif selectedTile.GetNumber() > 0:
            return False
        else:
            childTiles: list[Tile] = [selectedTile]
            while childTiles:
                # Get first tile in list.
                parentTile = childTiles.pop(0)
                parentCoords: tuple(int) = parentTile.GetCoordinate()
                children = self.__GetChildren(parentCoords)
                childTiles.extend(children)
            return False

    def __GetChildren(self, parentCoords: tuple(int)) -> list[Tile]:
        """
        Reveals all of the surround tiles and returns the ones that are empty.
        
        Args:
            parentCoords: The coordinates (x, y) of the parent node.
            
        Returns:
            List of empty tiles that have not been explored.
        """

        x, y = parentCoords
        listOfChildren = []
        for innerY in range(y - 1, y + 2):
            for innerX in range(x - 1, x + 2):
                try:
                    childTile = self.__2DTileArray[innerY][innerX]
                    if childTile.GetNumber() == 0 and not childTile.IsBomb() and not childTile.IsExplored():
                        listOfChildren.append(childTile)
                    childTile.SetExplored()
                except IndexError:
                    pass
        return listOfChildren