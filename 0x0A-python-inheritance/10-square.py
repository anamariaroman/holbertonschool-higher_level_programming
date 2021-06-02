#!/usr/bin/python3
"""
The Square class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Initializate"""
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
