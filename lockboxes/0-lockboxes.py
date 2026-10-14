#!/usr/bin/python3
"""Determine whether all boxes can be unlocked."""


def canUnlockAll(boxes):
    """Return True if all boxes can be opened, otherwise False."""
    if not boxes:
        return True

    opened = {0}
    keys = list(boxes[0])

    while keys:
        key = keys.pop()

        if key < len(boxes) and key not in opened:
            opened.add(key)
            keys.extend(boxes[key])

    return len(opened) == len(boxes)
