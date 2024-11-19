#!/usr/bin/python3
"""Rectangle class that defines a rectangle class by width and height"""


class Rectangle:
    """Rectangle class defined by width and height"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiates the rectangle object"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns the area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """Creates a string object from an object"""
        if self.__width == 0 or self.__height == 0:
            return ""
        area_rpr = []
        for i in range(self.__height):
            area_rpr.append("#" * self.__width)
        return "\n".join(area_rpr)

    def __repr__(self):
        """Returns a string representation of a rectangle"""
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """Deletes an instance object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
