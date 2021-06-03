#!/usr/bin/python3
""" This function have the class "Student" """


class Student:
    """ Students information """
    def __init__(self, first_name, last_name, age):
        """ Initializate """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """The directory"""
        if attrs is None:
            return self.__dict__
        else:
            new_aux = {}

            for i in attrs:
                if i in self.__dict__:
                    new_aux[i] = self.__dict__[i]
            return new_aux

    def reload_from_json(self, json):
        """ replaces the attributes of the class """
        for a in json:
            self.__dict__[a] = json[a]
