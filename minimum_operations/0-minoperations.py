#!/usr/bin/python3
"""Calculate the minimum operations to obtain n H characters."""


def minOperations(n):
    """Return the fewest operations needed to get n H characters."""
    if not isinstance(n, int) or n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
