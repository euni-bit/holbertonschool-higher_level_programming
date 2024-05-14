#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        for j in range(len(row)):
            print("{:d}".format(row[j]), end=" " if j < len(row) - 1 else "")
        print("")
