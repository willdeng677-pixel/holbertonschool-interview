#!/usr/bin/python3
"""
Module for solving the coin change problem.
"""
from collections import deque


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list of int): The values of the coins in possession.
        total (int): The target amount to meet.

    Returns:
        int: Fewest number of coins needed to meet total, or -1 if impossible.
    """
    if total <= 0:
        return 0

    queue = deque([(0, 0)])
    visited = {0}
    coins = sorted(set(coins), reverse=True)

    while queue:
        curr_amount, num_coins = queue.popleft()

        for coin in coins:
            next_amount = curr_amount + coin
            if next_amount == total:
                return num_coins + 1
            if next_amount < total and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, num_coins + 1))

    return -1
