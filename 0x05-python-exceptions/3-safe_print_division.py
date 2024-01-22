#!/usr/bin/python3
# This script defines a function safe_print_division that divides two integers.

def safe_print_division(a, b):
    """
    Divide two integers and print the result.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float or None: The value of the division, or None if division by 0 occurs.
    """
    result = None  # Initialize the result variable

    # Use try-except-finally block to handle exceptions
    try:
        result = a / b  # Perform the division
    except ZeroDivisionError:
        pass  # Handle division by 0
    finally:
        print("Inside result: {}".format(result))  # Print the result in the finally section

    return result  # Return the value of the division

# Test the function with examples
if __name__ == "__main__":
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))
