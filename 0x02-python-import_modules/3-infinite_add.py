#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    suma = 0
    for i in range(1, len(argv)):
        suma += int(argv[i])

    print("{:d}".format(suma))
