class Tile:
    """
    Use to represent a tile on the game board.
    """

    def __init__(self, x: int, y: int) -> None:
        """
        Initialises a the tile class.
        
        Args:
            x: The x-Coordinate of the tile.
            y: The y-Coordinate of the tile.
        """

        self.__coordinates = (x, y)
        self.__isExplored = False
        self.__isBomb = False
        self.__number = 0

    def __str__(self) -> str:
        if self.__isExplored and self.__isBomb:
            return "X"
        elif self.__isExplored and not self.__isBomb:
            return str(self.__number)
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
            Tile number.

        Raises:
            ValueError: if there is a bomb on this tile.
        """

        if self.__isBomb:
            raise ValueError("There is a bomb on this tile.")
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

    def GetCoordinate(self) -> tuple(int):
        """
        Gets the coordinate of the tile.
        
        Returns:
            The tiles coordiantes.
        """

        return self.__coordinates
    