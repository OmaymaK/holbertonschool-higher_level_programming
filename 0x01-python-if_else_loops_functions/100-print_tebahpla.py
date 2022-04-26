#!/usr/bin/python3
i = 122
while i > 96:
    if i % 2 == 0:
        c = i
    else:
        c = i - 32
    print("{:c}".format(c), end='')
    i -= 1
