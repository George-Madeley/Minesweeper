from random import randint
from typing import TypeAlias
from Tile import Tile

TileList: TypeAlias = list[Tile]

class Board:
    def __init__(self, sizeX: int, sizeY: int, maxBombs: int) -> None:
        self.__2DTileArray = [[Tile(x,y) for x in range(sizeX)] for y in range(sizeY)]
        self.__sizeX = sizeX
        self.__sizeY = sizeY
        self.__bombs: TileList = self.GenerateBombs(maxBombs)

    def __str__(self) -> str:
        """
        Foramts the string representation of the board and returns it.
        """

        boardString = "\t|"
        borderString= "\t|"
        for i in range(self.__sizeX):
            if len(str(i)) == 1:
                boardString += f" {i} "
            elif len(str(i)) == 2:
                boardString += f" {i}"
            borderString += "___"
        boardString += f"\n{borderString}\n"
        for index, tileArray in enumerate(self.__2DTileArray):
            boardString += f"{str(index)}\t|"
            for tile in  tileArray:
                boardString += str(f" {str(tile)} ")
            boardString += "\n"
        return boardString

    def AreAllBombsFound(self) -> bool:
        """
        Checks if all bombs have been found.
        
        Returns:
            True if all bombs have been found.
        """
        for bombTile in self.__bombs:
            if not bombTile.IsFlagged():
                return False
        return True

    def GenerateBombs(self, maxBombs: int) -> list:
        """
        Generates a given amount of bombs and places them onto the board.

        Args:
            maxBombs: The number of bombs to be placed onto the board.

        Returns:
            A list of all the bombs.
        """

        listOfBombs = []
        bombsGenerated = int(maxBombs)
        while bombsGenerated > 0:
            x = randint(0, self.__sizeX)
            y = randint(0, self.__sizeY)
            try:
                bombTile: Tile = self.__2DTileArray[y][x]
                if bombTile.IsBomb():
                    continue
                bombTile.SetBomb()
                self.IncrementSurroundingTiles(x, y)
                bombsGenerated -= 1
                listOfBombs.append(bombTile)
            except IndexError:
                pass
        return listOfBombs

    def IncrementSurroundingTiles(self, x: int, y: int) -> None:
        """
        Increments the surrounding tiles of a bomb by one.

        Args:
            x: The X-coordinate of a bomb.
            y: The Y-coordinate of a bomb.
        """

        for innerY in range(y - 1, y + 2):
            for innerX in range(x - 1, x + 2):
                if innerX < 0 or innerX >= self.__sizeX or innerY < 0 or innerY >= self.__sizeY:
                    continue
                if innerX == x and innerY == y:
                    continue
                try:
                    surroundingTile: Tile = self.__2DTileArray[innerY][innerX]
                    surroundingTile.IncrementNumber()
                except IndexError:
                    pass

    def PlaceFlag(self, x: int, y: int) -> None:
        """
        Places a flag onto the board.
        
        Args:
            x: The X-Coordinate of the flag.
            y: The Y-Coordinate of the flag.
        """
        try:
            flaggedTile = self.__2DTileArray[y][x]
            flaggedTile.SetFlag()
        except IndexError:
            print("The coordinates you hvae entered are out of bounds. Please try again.")

    def RevealTiles(self, x: int, y: int) -> bool:
        """
        Reveals selected and any other tiles.
        
        Args:
            x: The X-coordinate of the selected tile.
            y: The Y-coordinate of the selected tile.

        Returns:
            True if the tile was a bomb.
        """

        selectedTile = self.__2DTileArray[y][x]
        selectedTile.SetExplored()
        if selectedTile.IsBomb():
            return True
        elif selectedTile.GetNumber() > 0:
            return False
        else:
            childTiles = [selectedTile]
            while childTiles:
                # Get first tile in list.
                parentTile = childTiles.pop(0)
                parentCoords = parentTile.GetCoordinate()
                children = self.__GetChildren(parentCoords)
                childTiles.extend(children)
            return False

    def __GetChildren(self, parentCoords: any) -> any:
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
                    if innerX < 0 or innerX >= self.__sizeX or innerY < 0 or innerY >= self.__sizeY:
                        continue
                    childTile = self.__2DTileArray[innerY][innerX]
                    if childTile.GetNumber() == 0 and not childTile.IsBomb() and not childTile.IsExplored():
                        listOfChildren.append(childTile)
                    childTile.SetExplored()
                except IndexError:
                    pass
        return listOfChildren