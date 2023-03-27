#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
            elements = elements + 1
        print()
        return x
    except IndexError:
        print()
        return elements
