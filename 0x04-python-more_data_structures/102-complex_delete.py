#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for x, y in a_dictionary.items():
        if y == value:
            del a_dictionary[x]
            break
    return a_dictionary
