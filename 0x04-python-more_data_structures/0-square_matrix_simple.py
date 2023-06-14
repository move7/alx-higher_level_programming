#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = []
    for row in matrix:
        row_square = []
        for i in row:
            row_square.append(i ** 2)
        matrix_square.append(row_square)
    return matrix_square
