#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        a = 0
        b = 0
        for tup in my_list:
            (w, o) = tup
            a += (w * o)
            b += o
        return (a / b)
