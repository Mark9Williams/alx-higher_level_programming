#!/usr/bin/python3
""" class Square that defines a square """


class Square:
    """ Class that defines a square """

    def __init__(self, size=0, position=(0, 0)):
        """ Method to initialize the square object """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Retrives position """
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the values of position """
        if (not isinstance(value, tuple) and all()
                and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Method to calculate the area of the square """
        return self.__size ** 2

    def my_print(self):
        """ Method to print the square with # """
        if self.__size == 0:
            print()
            return

        # Add vertical spaces based on position[1]
        print("\n" * self.__position[1], end="")
        # Print the square rows with spaces for position[0]
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        if self.__size == 0:
            return ""
        square_str = "\n" * self.__position[1]
        for i in range(self.__size):
            square_str += " "*self.__position[0] + "#" * self.__size + "\n"
        return square_str.rstrip()
