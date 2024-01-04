#!/usr/bin/python3
# 0_add.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Main function to calculate the sum of 1 and 2."""
    # Importing the add function from add_0 module
    from add_0 import add

    # Assigning values to variables a and b
    a = 1
    b = 2

    # Printing the addition of variables a and b
    print("{} + {} = {}".format(a, b, add(a, b)))
