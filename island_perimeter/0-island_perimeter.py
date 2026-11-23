#!/usr/bin/python3
"""
Module for calculating the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid where 0 is water and 1 is land.

    Returns:
        int: The total perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
