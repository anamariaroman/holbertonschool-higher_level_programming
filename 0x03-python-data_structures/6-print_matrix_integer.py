#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    else:
        for i in matrix:
            length = len(i)

            for a in range(0, length):

                if a < length - 1:
                    print("{:d}".format(i[a]), end=' ')

                else:
                    print("{:d}".format(i[a]))
