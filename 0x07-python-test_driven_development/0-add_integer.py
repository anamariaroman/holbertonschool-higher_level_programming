#!/usr/bin/python3
"""
    Module create function that adds 2 integers
	and return a + b
"""


def add_integer(a, b=98):
    """ This function adds 2 integers """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
