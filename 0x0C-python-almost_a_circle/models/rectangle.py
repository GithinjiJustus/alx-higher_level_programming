#!/usr/bin/python3
"""Defines the Rectangle class."""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The identity of the rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get or set the x-coordinate of the rectangle's position."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get or set the y-coordinate of the rectangle's position."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
        
    def area(self):
        """Return the area value of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with the character #."""
        for _ in range(self.height):
            print("#" * self.width)

    def display(self):
        """Print the Rectangle instance with the character #."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Return a string representation of the Rectangle."""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """Update the attributes of the Rectangle."""
        attr_names = ["id", "width", "height", "x", "y"]
        for i in range(len(args)):
            setattr(self, attr_names[i], args[i])

    def update(self, *args, **kwargs):
        """Update the attributes of the Rectangle."""
        attr_names = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attr_names[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attr_names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
