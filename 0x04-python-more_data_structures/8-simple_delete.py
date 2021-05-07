#!/usr/bin/python3
def simple_delete(a_dictionary, the_key=""):
    if the_key in a_dictionary:
        del a_dictionary[the_key]
    return a_dictionary
