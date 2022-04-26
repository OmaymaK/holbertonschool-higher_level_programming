#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(97, 123):
            upper = ord(c) - 32
        else:
            upper = ord(c)
        print("{:c}".format(upper), end="")
    print("")
