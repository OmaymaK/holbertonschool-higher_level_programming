#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a1 = tuple_a or (0, 0)
    tuple_b1 = tuple_b or (0, 0)
    if len(tuple_a) == 1:
        tuple_a1 = (tuple_a[0], 0)
    if len(tuple_b) == 1:
        tuple_b1 = (tuple_b[0], 0)
    return (tuple_a1[0] + tuple_b1[0], tuple_a1[1] + tuple_b1[1])
