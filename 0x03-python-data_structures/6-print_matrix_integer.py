#!/usr/bin/bash
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            print("{}".format(i), end='')
        print()
