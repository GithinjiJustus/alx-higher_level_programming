#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Rectangle class with private attributes width and height"""
    number_of_instances = 0  # Class attribute to count instances
    print_symbol = "#"  # Class attribute for string representation

    def __init__(self, width=0, height=0):
        """Initializes a new instance with optional width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance count

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(str(self.print_symbol) * self.__width for _ in range(self.__height)))

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement instance count

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares the area of two rectangles and returns the larger one
        If both have the same area, returns rect_1
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with equal width and height"""
        return cls(size, size)
