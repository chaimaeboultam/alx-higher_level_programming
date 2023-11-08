#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = [
        [element ** 2 for element in sub_matrix]
        for sub_matrix in matrix
    ]
    return squared_matrix
