#!/usr/bin/python3
""" task 1 """


def write_file(filename="", text=""):
    """ Writing a string to a file """
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(text)
    return len(text)
