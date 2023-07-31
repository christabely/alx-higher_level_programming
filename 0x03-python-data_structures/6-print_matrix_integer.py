#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            if k != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][k]), end='')
        print()
