#!/usr/bin/python3
""" Task 9  """


class Student:
    """ Class Student """

    def __init__(self, first_name, last_name, age):
        """ initialsation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Dictionary representation of Student"""
        return self.__dict__
