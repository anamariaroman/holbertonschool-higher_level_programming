#!/usr/bin/python3
"""
Rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """height getter."""
        return self.__width

    @property
    def height(self):
        """height getter."""
        return self.__height

    @property
    def x(self):
        """x getter."""
        return self.__x

    @property
    def y(self):
        """y getter."""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and returns the area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Print in stdout the Rectangle with the character #"""
        for i in range(self.__y):
            print("" * self.__y)

        for i in range(self.__height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
		str representation.
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            Assigns an argument to the following attributes.
        """
        keys = ["id", "width", "height", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in keys:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
            Returns the dictionary representation of the Rectangle class.
        """
        d = dict()
        d["x"] = self.x
        d["y"] = self.y
        d["id"] = self.id
        d["height"] = self.height
        d["width"] = self.width

        return (d)
