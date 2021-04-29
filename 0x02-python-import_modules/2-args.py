#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    l = len(argv) - 1
    count = 0
    args = "{:d} argument"

    if l == 1:
        args = args
    else:
        args = args + "s"

    if l == 0:
        args = args + "."
    else:
        args = args + ":"

    print(args.format(l))

    for arg in argv:
        if count:
            print("{:d}: {:s}".format(count, arg))
        count = count + 1
