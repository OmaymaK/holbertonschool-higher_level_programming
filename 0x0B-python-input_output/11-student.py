#!/usr/bin/python3
""" Task 10  """


class Student:
    """ Class Student """

    def __init__(self, first_name, last_name, age):
        """ initialsation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Dictionary representation of Student"""
        if type(attrs) is not list:
            return self.__dict__
        else:
            dic = {}
        for a in attrs:
            if a in self.__dict__.keys():
                dic[a] = self.__dict__[a]
        return dic

    def reload_from_json(self, json):
        """replaces all attributes of the student"""
        for keys in json:
            setattr(self, keys, json[keys])
