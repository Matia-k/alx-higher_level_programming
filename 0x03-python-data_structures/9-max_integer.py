#!/usr/bin/python3
def max_integer(my_list=[]):
    bigest = 0
    list_len = len(my_list)
    i = 0

    if list_len == 0:
        return None

    while (i < list_len):
        if my_list[i] > bigest:
            bigest = my_list[i]
        i = i + 1

    return bigest
