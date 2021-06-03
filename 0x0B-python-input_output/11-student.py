#!/usr/bin/python3
""" This function have the class "Student" """


class Student:
    """ List of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns the dictionary"""
        return self.__dict__
