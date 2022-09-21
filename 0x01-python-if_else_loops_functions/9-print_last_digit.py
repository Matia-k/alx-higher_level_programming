#!/usr/bin/python3
def print_last_digit(number):
    n = str(number)[-1]
    print(f"{n}", end='')
    return int(n)
