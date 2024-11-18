#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ Class that defines a square """

    def __init__(self, size=0):
        """ Method to initialize the square object """
        self.size = size

    @property
    def size(self):
        """ Retrieves thee value of size """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Method to calculate the area of the square """
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparison based on the area"""
        if isinstance(other, Square):
            return self.area() == other.area()

    def __ne__(self, other):
        """Inequality comaprison based on the area"""
        if isinstance(other, Square):
            return self.area() != other.area()

    def __gt__(self, other):
        """Greather than comaprison based on the area"""
        if isinstance(other, Square):
            return self.area() > other.area()

    def __ge__(self, other):
        """Greater or equal to comparison based on area"""
        if isinstance(other, Square):
            return self.area() >= other.area()

    def __lt__(self, other):
        """Lessthan comparison based on area"""
        if isinstance(other, Square):
            return self.area() < other.area()

    def __le__(self, other):
        """Lessthan or equal to comparison based on area"""
        if isinstance(other, Square):
            return self.area() <= other.area()
