#!/usr/bin/python3
"""Define a Square class."""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size for the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal in area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal in area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """Check if one square is greater than the other in area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if one square is greater than or equal to the other in area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if greater or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """Check if one square is less than the other in area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """Check if one square is less than or equal to the other in area.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if less or equal, False otherwise.
        """
        return self.area() <= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
