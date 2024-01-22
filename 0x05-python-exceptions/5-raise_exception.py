#!/usr/bin/python3
# This script defines a function raise_exception that raises a type exception.

def raise_exception():
    """
    Raise a type exception.

    Raises:
        TypeError: Always raises a type exception.
    """
    raise TypeError("This is a type exception")

# Test the function with examples
if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
