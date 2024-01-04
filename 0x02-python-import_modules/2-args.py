#!/usr/bin/python3
# 2-args.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Prints the count and list of arguments passed."""
    import sys

    # Calculate the count of arguments
    count = len(sys.argv) - 1

    # Checking the number of arguments and printing accordingly
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Printing each argument with its index
    for i in range(count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
