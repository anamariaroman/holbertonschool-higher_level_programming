#!/usr/bin/python3
"""
Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Init the square."""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Size getter."""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        str representation.
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
            Assigns an argument following attributes
        """
        keys = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, keys[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in keys:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
            Returns the dict Rectangle.
        """
        d = dict()
        d["id"] = self.id
        d["x"] = self.x
        d["size"] = self.size
        d["y"] = self.y

        return (d)
