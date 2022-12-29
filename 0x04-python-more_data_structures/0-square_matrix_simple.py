#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[row[i]**2 for row in matrix] for i in range(len(matrix))]
    return new_matrix


square_matrix_simple()
