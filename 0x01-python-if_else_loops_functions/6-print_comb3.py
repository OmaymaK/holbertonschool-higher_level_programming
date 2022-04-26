#!/usr/bin/python3
for i in range(0, 100):
    d = i % 10
    n = i / 10
    if n < d and i != 89:
        print("{:02d}, ".format(i), end="")
    elif i == 89:
        print("{:02d}".format(i))
