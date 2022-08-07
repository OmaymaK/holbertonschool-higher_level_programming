#!/usr/bin/python3
""" Task 3 """


def append_write(filename="", text=""):
    """ Appending to a text file """
    with open(filename, mode='a', encoding='utf-8') as f:
        f.write(text)
    return len(text)
