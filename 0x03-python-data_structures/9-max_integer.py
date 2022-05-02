def max_integer(my_list=[]):
    if not my_list:
        return None
    comp = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > comp:
            comp = my_list[i]
    return comp
