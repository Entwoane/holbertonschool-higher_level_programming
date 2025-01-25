#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix

    Args:
        matrix (list of lists): matrix of integers/floats
        div (int or float): number to divide by

    Returns: New Matrix with divided numbers rounded to 2 decimals

    Raises:
        TypeError: if matrix is not a list of lists of int or float
        TypeError: if rows of the matrix are not the same size
        TypeError: if div is not a number (int or float)
        ZeroDivisionError: if div equal 0
    """
    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[0.0 if div == float else round(element / div, 2) for element in row] for row in matrix]
