#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The 2-matrix_divided module supplies one function, matrix_divided(matrix, div).
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix by div

    args:
        matrix {[type]}: [description]
        fiv {[type]}: [description]
    """
    err1 = "matrix must be a matrix (list of lists) of integers/floats"
    err2 = "Each row of the matrix must have the same size"
    err3 = "div must be a number"
    err4 = "division by zero"

    if type(matrix) != list:
        raise TypeError(err1)

    size_row = None
    for row in matrix:
        if type(row) != list:
            raise TypeError(err1)
        if size_row is None:
            size_row = len(row)
        elif size_row != len(row):
            raise TypeError(err2)
        for element in row:
            if type(element)is not int and type(element) is not float:
                raise TypeError(err1)
    if type(div) is not int and type(div) is not float:
        raise TypeError(err3)

    if div == 0:
        raise ZeroDivisionError(err4)

    return [[round(element / div, 2) for element in row] for row in matrix]
