#!/usr/bin/python3
# This script defines a function raise_exception_msg that raises a name exception with a message.

def raise_exception_msg(message=""):
    """
    Raise a name exception with a message.

    Args:
        message (str): Optional message to include in the exception.

    Raises:
        NameError: Always raises a name exception with an optional message.
    """
    raise NameError(message)

# Test the function with examples
if __name__ == "__main__":
    try:
        raise_exception_msg("C is fun")
    except NameError as ne:
        print(ne)
