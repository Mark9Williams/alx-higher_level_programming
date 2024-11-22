#!/usr/bin/python3
"""a class Rectangle that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Instantiation method"""
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        """returns the area of a rectanle"""
        return self.__height * self.__width

    def __str__(self):
        """Returns a string representation of a rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
