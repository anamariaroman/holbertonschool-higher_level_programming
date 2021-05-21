#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """
    Defines a rectangle
    Attributes:
    width: width a rectangle
    height: heigth a rectangle
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Init
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        aux = ""
        if self.__width == 0 or self.__height == 0:
                return aux
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    aux += '#'
                aux += '\n'
            return aux[:-1]

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
