#!/usr/bin/python3
"""Define a MagicClass class."""


class MagicClass:
    """Represent a MagicClass."""
    def __init__(self, radius=0):
        """Initialize a new MagicClass.

        Args:
            radius (int or float): The radius of the MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate the area of the MagicClass.

        Returns:
            float: The area of the MagicClass.
        """
        return self.__radius ** 2 * 3.14159265359

    def circumference(self):
        """Calculate the circumference of the MagicClass.

        Returns:
            float: The circumference of the MagicClass.
        """
        return 2 * 3.14159265359 * self.__radius


if __name__ == "__main__":
    import dis

    dis.dis(MagicClass)
