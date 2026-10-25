#!/usr/bin/python3

import sys
import re


def print_stats(total_size, status_codes):
    """Print accumulated file size and status code counts."""
    print("File size: {}".format(total_size))

    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    status_codes = {}
    valid_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    line_count = 0

    pattern = re.compile(
        r'^\S+ - \[.*?\] "GET /projects/260 HTTP/1\.1" '
        r'(\d{3}) (\d+)$'
    )

    try:
        for line in sys.stdin:
            line_count += 1
            line = line.strip()

            match = pattern.match(line)
            if match:
                status = int(match.group(1))
                size = int(match.group(2))

                total_size += size

                if status in valid_status_codes:
                    status_codes[status] = status_codes.get(status, 0) + 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
