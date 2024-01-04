#!/usr/bin/python3
# 1-calculation.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Performing basic calculations on numbers."""
    # Importing add, sub, mul, and div functions from calculator_1 module
    from calculator_1 import add, sub, mul, div

    # Assigning values to variables a and b
    a = 10
    b = 5

    # Printing the sum of a and b
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Printing the difference of a and b
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Printing the product of a and b
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Printing the division of a by b
    print("{} / {} = {}".format(a, b, div(a, b)))
