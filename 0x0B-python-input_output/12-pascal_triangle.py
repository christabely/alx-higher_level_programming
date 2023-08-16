#!/usr/bin/python3
"""
This function makes a pascal triangle
"""


def pascal_triangle(n):
    """
    This function is a representation of a pascal triangle.
    """
    if (n <= 0):
        return ([])
    elif (n == 1):
        return ([[1]])
    elif (n == 2):
        return ([[1], [1, 1]])

    pascal = [[1], [1, 1]]

    for i in range(1, n - 1):
        new_list = []
        new_list.append(1)
        for j in range(1, len(pascal)):
            new_list.append(pascal[i][j - 1] + pascal[i][j])
        new_list.append(1)
        pascal.append(new_list)

    return (pascal)
