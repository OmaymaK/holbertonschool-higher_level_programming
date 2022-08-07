#!/usr/bin/python3
""" task 5 """


def inherits_from(obj, a_class):
    """ check inheritance """

    if a_class in list(obj.__class__.__mro__)[1:]:
        return True
    else:
        return False
