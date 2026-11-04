#!/usr/bin/env python3
"""Determine if a dataset represents a valid UTF-8 encoding."""


def validUTF8(data):
    """Return True if data is valid UTF-8, otherwise False."""

    remaining_bytes = 0

    for num in data:
        # Only consider the 8 least significant bits
        byte = num & 0xFF

        if remaining_bytes == 0:
            # 1-byte character: 0xxxxxxx
            if (byte >> 7) == 0:
                continue

            # 2-byte character: 110xxxxx
            elif (byte >> 5) == 0b110:
                remaining_bytes = 1

            # 3-byte character: 1110xxxx
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2

            # 4-byte character: 11110xxx
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3

            # Invalid leading byte
            else:
                return False

        else:
            # Continuation byte must start with 10
            if (byte >> 6) != 0b10:
                return False

            remaining_bytes -= 1

    # All characters must have their required bytes
    return remaining_bytes == 0
