#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    i = 0
    string_len = len(my_string)
    while (i < string_len):
        if (my_string[i] == 'c' or my_string[i] == 'C'):
            i = i + 1
            continue
        else:
            new_string = new_string + my_string[i]
        i = i + 1
    return new_string
