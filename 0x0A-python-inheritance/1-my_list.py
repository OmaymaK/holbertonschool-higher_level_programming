#!/usr/bin/python3
"""task 1"""


class MyList(list):
    """ inhereting from list"""

    def print_sorted(self):
        a = sorted(self)
        print(a)
