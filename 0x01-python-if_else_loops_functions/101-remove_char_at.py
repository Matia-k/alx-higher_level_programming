#!/usr/bin/python3
def remove_char_at(str, n):
    new_string = ""

    for index in range(len(str)):
        if index == n:
            continue
        new_string += str[index]

    return new_string
