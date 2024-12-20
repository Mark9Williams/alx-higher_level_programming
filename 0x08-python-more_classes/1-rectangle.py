#!/usr/bin/python3
"""Rectangle class that defines a rectangle class by width and height"""


class Rectangle:
    """Rectangle class defined by width and height"""

    def __init__(self, width=0, height=0):
        """Instantiates the rectangle object"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        "Retrieves the height"
        return self.__height

    @height.setter
    def height(self, value):
        "Sets the height of a rectangle"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
