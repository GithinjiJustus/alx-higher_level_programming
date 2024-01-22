#!/usr/bin/python3
"""
This script defines a function safe_print_integer_err that prints an integer.
"""

import sys

def safe_print_integer_err(value):
    """
    Prints an integer and handles errors.

    Args:
        value: Any type (integer, string, etc.).

    Returns:
        bool: True if value is an integer and has been correctly printed,
              False otherwise.

    Raises:
        Exception: Prints an error message to stderr in case of an exception.
    """
    try:
        # Attempt to print the integer value
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        # Handle errors and print an error message to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return False

# Test the function with examples
if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer_err(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
