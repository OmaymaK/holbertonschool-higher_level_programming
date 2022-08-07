#!/usr/bin/python3
""" Task 12 """


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal’s triangle of n """
    lists = []
    if n <= 0:
        return lists
    else:
        for i in range(n):
            lists.append([])
            for j in range(i+1):
                if i > 1 and j < i and j != 0:
                    lists[i].append(lists[i-1][j] + lists[i-1][j-1])
                elif j != n:
                    lists[i].append(1)
        return lists
