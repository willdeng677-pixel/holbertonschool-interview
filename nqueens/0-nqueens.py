#!/usr/bin/python3
"""Solve the N Queens problem."""

import sys


def solve_nqueens(n):
    """Find and print all possible solutions."""

    solutions = []
    positions = []

    columns = set()
    diagonals1 = set()
    diagonals2 = set()

    def backtrack(row):
        """Try placing a queen in each column of the current row."""

        if row == n:
            solutions.append(positions.copy())
            return

        for col in range(n):
            # Check if the position is safe
            if (col in columns or
                    row - col in diagonals1 or
                    row + col in diagonals2):
                continue

            # Place the queen
            positions.append([row, col])
            columns.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)

            # Move to the next row
            backtrack(row + 1)

            # Backtrack: remove the queen
            positions.pop()
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)

    backtrack(0)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":

    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check whether N is an integer
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check whether N is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
