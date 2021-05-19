#!/usr/bin/python3
"""Definition square class"""


class Square:
    """Class.
    Attributes:
        __size: size of the square.
    """

    def __init__(self, size=0):
        """Init the Square"""
        self.__size = size
    @property
    def size(self):
        """Returns the size square"""
        return self.__size
    @size.setter
    def size(self, size):
        """set __size"""
        if type(size) is not int:
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns the size square."""
        return self.__size * self.__size
    def my_print(self):
        """print stdout the square with the character #"""
	for x in range(0, self.__size):
            for y in range(0, self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
