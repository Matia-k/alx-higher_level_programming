#!/usr/bin/python3
def max_integer(my_list=[]):
    big = 0
    for num in my_list:
        if num > big:
            big = num

    return big
