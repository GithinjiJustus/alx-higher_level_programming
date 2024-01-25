#!/usr/bin/python3

def add_integer(a, b=98):
    """Add two numbers and return the result."""

    # Check if 'a' is an integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("Parameter 'a' must be an integer or float")

    # Check if 'b' is an integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("Parameter 'b' must be an integer or float")

    # Return the sum of 'a' and 'b' after converting to integers
    return int(a) + int(b)
