#!/usr/bin/python3
# 3-infinite_add.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Prints the sum of all arguments provided."""
    import sys

    total = 0
    # Iterating through the arguments and adding them to the total
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])

    # Printing the total sum of arguments
    print("{}".format(total))
