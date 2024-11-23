#!/usr/bin/python3
"""A script that reads standard inpu line by line and computes metrics"""
import sys


def print_stats(total_size, status_count):
    """prints the status counts"""
    print(f"File size: {total_size}")
    for status in sorted(status_count.keys()):
        print(f"{status}: {status_count[status]}")


def main():
    """This is the main function of the program"""
    total_size = 0
    status_count = {}
    line_count = 0
    valid_input = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()

                file_size = int(parts[-1])
                status_code = int(parts[-2])

                total_size += file_size
                if status_code in valid_input:
                    if status_code not in status_count.keys():
                        status_count[status_code] = 0
                    status_count[status_code] += 1
                    line_count += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_count)

            except (IndexError, ValueError):
                # skip malformed lines
                continue
    except KeyboardInterrupt:
        print_stats(total_size, status_count)
        raise
    print_stats(total_size, status_count)


if __name__ == "__main__":
    main()
