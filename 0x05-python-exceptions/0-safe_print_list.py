#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    variable = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            variable += 1
    except IndexError:
        pass
    print()
    return variable
