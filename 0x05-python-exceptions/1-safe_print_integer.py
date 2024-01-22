#!/usr/bin/python3
# This script defines a function safe_print_integer that prints an integer.

def safe_print_integer(value):
    """
    Print an integer using "{:d}".format().

    Args:
        value: Any type of value (integer, string, etc.).

    Returns:
        bool: True if value has been correctly printed (it means the value is an integer),
              False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False

# Test the function with examples
if __name__ == "__main__":
    value = 89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = -89
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))

    value = "School"
    has_been_print = safe_print_integer(value)
    if not has_been_print:
        print("{} is not an integer".format(value))
