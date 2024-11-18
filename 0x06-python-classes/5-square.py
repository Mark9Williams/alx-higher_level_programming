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

    def my_print(self):
        """ Method to print the square with # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)