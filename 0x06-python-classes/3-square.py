#!/usr/bin/python3
"""Definition square class"""


class Square:
    """class"""

    def __init__(self, size=0):
        """Constructor to initialize the attributes"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
            return
        if size < 0:
            raise ValueError("size must be >= 0")
            return

        self.__size = size

    def area(self):
        """Return the square size"""
        return self.__size ** 2

