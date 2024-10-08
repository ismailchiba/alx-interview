#!/usr/bin/python3
"""
    Pascal Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of height n.

    Args:
        n (int): The number of rows in Pascal's triangle.
                  Must be a non-negative integer.

    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle.
                          Returns an empty list if n <= 0.

    Example:
        >>> pascal_triangle(5)
        [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    if n <= 0:
        return []
    else:
        res = [[1]]
        for i in range(n - 1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res
