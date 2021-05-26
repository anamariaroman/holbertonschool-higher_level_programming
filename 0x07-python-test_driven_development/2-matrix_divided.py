#!/usr/bin/python3
"""Function that
	divides matrix"""


def matrix_divided(matrix, div):
    new = []
    j = 0
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    for m in matrix:
        if len(m) != length:
            raise TypeError("Each row of the matrix must have the same size")
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        new.append([])
        for a in i:
            res = round(a / div, 2)
            if type(a) != int and type(a) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new[j].append(res)
        j += 1
    return(new)
