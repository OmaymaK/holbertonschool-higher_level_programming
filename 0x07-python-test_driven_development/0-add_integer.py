#!/usr/bin/python3
def add_integer(a, b=98):
    """ Function that adds two integers
    Agruments:
        a : must be int
        b : must be int
    Return:
        int: Sum of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
