#!/usr/bin/python3
"""
Module Pascal Triangle
"""


def pascal_triangle(n):
    """pascal_triangle """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    triangle = [
            [1],
            [1, 1]]
    for i in range(1, n-1):
        row = [1]
        for j in range(0, len(triangle[i]) - 1):
            row.extend([triangle[i][j] + triangle[i][j+1]])
        row += [1]
        triangle.append(row)
    return triangle
