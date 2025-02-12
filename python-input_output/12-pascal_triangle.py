#!/usr/bin/python3
"""
This module provides a function to generate Pascal's Triangle.

The `pascal_triangle` function calculates Pascal's Triangle up to a specified
number of rows and returns it as a list of lists.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to `n` rows.

    Pascal's Triangle is a triangular array of the binomial coefficients. Each
    number in the triangle is the sum of the two numbers directly above it.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        list: A list of lists, where each inner list
        represents a row in Pascal's Triangle.
        If `n` is less than or equal to 0, an empty list is returned.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
