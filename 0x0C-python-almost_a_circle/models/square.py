#!/usr/bin/python3
"""Defines the Square class."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.
        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position.
            y (int): The y-coordinate of the square's position.
            id (int): The identity of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return a string representation of the Square."""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update the attributes of the Square."""
        attr_names = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attr_names[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr_names:
                    setattr(self, key, value)
