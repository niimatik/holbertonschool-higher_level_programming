#!/usr/bin/python3
"""
pascal_triangle Module

This module provides a function to generate Pascal's Triangle up to a given
number of rows.

The main function, `pascal_triangle(n)`, returns a list of lists of integers
representing the first `n` rows of Pascal's Triangle. This structure is
useful in combinatorics, mathematics, and algorithm practice.
"""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Pascal's Triangle is a triangular array of the binomial coefficients.
    Each number is the sum of the two numbers directly above it in the
    previous row.

    Args:
        n (int): The number of rows to generate in the triangle.

    Returns:
        list of list of int: A list of lists representing Pascal's Triangle.
        Each inner list corresponds to a row in the triangle.
    """
    if n <= 0:
        return []

    limit = n - 1
    triangle = [[1]]

    for i in range(limit):
        row = []
        row.append(1)

        if len(triangle[i]) > 1:
            prev_row_len = len(triangle[i]) - 1
            nxt = 1

            for j in range(prev_row_len):
                suma = triangle[i][j] + triangle[i][nxt]
                row.append(suma)
                nxt += 1

        row.append(1)
        triangle.append(row)

    return triangle
