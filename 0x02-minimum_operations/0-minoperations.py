#!/usr/bin/python3
"""
Solution to minOperations problem
"""


def minOperations(n):
    """
    write a method that calculates the fewest number
    of operations needed to result in exactly n H characters
    """
    if n <= 1:
        return 0

    operation = 0
    divisor = 2

    while (n > 1):
        while (n % divisor == 0):
            operation += divisor
            n //= divisor
        divisor += 1
    return operation
