#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for n in row:
            print("{}".format(n), end=" ")
        print()