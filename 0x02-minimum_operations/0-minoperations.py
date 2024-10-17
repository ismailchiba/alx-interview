#!/usr/bin/python3
""" Minimum operations """


def minOperations(n: int) -> int:
    """ Minimum operations

    Keyword arguments:
    n -- number to evaluate
    Return: number of operations or 0
    """

    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return i + minOperations(n // i)
    return 0
