class Tile:
    """
    Use to represent a tile on the game board.
    """

    def __init__(self, x: int, y: int, isExplored: bool = False) -> None:
        """
        Initialises a the tile class.
        
        Args:
            x: The x-Coordinate of the tile.
            y: The y-Coordinate of the tile.
            isExplored: If the tile is explored (default: False)
        """

        self.__coordinates = (x, y)
        self.__isExplored = isExplored
        self.__isBomb = False
        self.__number = 0
        self.__isFlagged = False

    def __str__(self) -> str:
        if self.__isExplored and self.__isBomb:
            return "X"
        elif self.__isExplored:
            if self.__number > 0:
                return str(self.__number)
            else:
                return " "
        elif self.__isFlagged:
            return "P"
        else:
            return "-"


    def SetBomb(self) -> None:
        """
        Set bomb true.
        """

        self.__isBomb = True

    def IsBomb(self) -> bool:
        """
        Checks if the tile is a bomb.
        
        Returns:
            True if the tile is a bomb.
        """

        return self.__isBomb

    def GetNumber(self) -> int:
        """
        Gets the tile number indicating number of surronding bombs.
        
        Returns:
            Tile number. Nine if bomb.
        """

        if self.__isBomb:
            return 9
        else:
            return self.__number

    def IncrementNumber(self) -> None:
        """
        Increments tile number by one.

        Raises:
            ValueError: if number exceeds eight.
        """
        
        self.__number += 1
        if self.__number > 8:
            raise ValueError("Tile number has exceeded eight")

    def IsExplored(self) -> bool:
        """
        Checks if the tile has been explored.
        
        Returns:
            True if the tile has been explored.
        """

        return self.__isExplored

    def SetExplored(self) -> None:
        """
        Sets the explored to True.
        """

        self.__isExplored = True

    def GetCoordinate(self) -> any:
        """
        Gets the coordinate of the tile.
        
        Returns:
            The tiles coordiantes.
        """

        return self.__coordinates
    
    def SetFlag(self) -> None:
        """
        Sets isFlagged to True.
        """
        self.__isFlagged = True

    def IsFlagged(self) -> bool:
        """
        Checks if the tile has been flagged.
        
        Returns:
            True if the tile has been flagged.
        """
        return self.__isFlagged