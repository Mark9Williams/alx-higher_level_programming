#!/usr/bin/python3
"""Implementation of a Square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square that inherits from a Rectangle"""

    def __init__(self, size):
        """instantiation method"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns area of a square"""
        return self.__size**2

    def __str__(self):
        """returns string representation of a square"""
        return f"[Square] {self.__size}/{self.__size}"
