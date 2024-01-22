#!/usr/bin/python3
"""
This script defines a function safe_function that executes a function safely.
"""

import sys

def safe_function(fct, *args):
    """
    Executes a function safely.

    Args:
        fct: A pointer to a function.
        *args: Variable number of arguments to be passed to the function.

    Returns:
        result: Result of the function.

    Raises:
        Exception: Prints an error message to stderr in case of an exception.
    """
    try:
        # Attempt to execute the provided function with given arguments
        result = fct(*args)
        return result
    except Exception as e:
        # Handle errors and print an error message to stderr
        print("Exception: {}".format(e), file=sys.stderr)
        return None

# Test the function with examples
if __name__ == "__main__":
    def my_div(a, b):
        return a / b

    result = safe_function(my_div, 10, 2)
    print("result of my_div: {}".format(result))

    result = safe_function(my_div, 10, 0)
    print("result of my_div: {}".format(result))

    def print_list(my_list, length):
        i = 0
        while i < length:
            print(my_list[i])
            i += 1
        return length

    result = safe_function(print_list, [1, 2, 3, 4], 10)
    print("result of print_list: {}".format(result))
