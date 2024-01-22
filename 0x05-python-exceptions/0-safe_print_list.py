#!/usr/bin/python3
# This script defines a function safe_print_list that prints elements of a list.

def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.
    
    Args:
        my_list (list): List containing any type of elements.
        x (int): Number of elements to print.

    Returns:
        int: The real number of elements printed.
    """
    nb_printed = 0  # Initialize the count of printed elements

    # Use try-except block to handle exceptions
    try:
        for i in range(x):
            print(my_list[i], end="")
            nb_printed += 1
    except IndexError:
        pass  # Ignore index errors
    
    print()  # Print a new line after the elements
    return nb_printed  # Return the real number of elements printed

# Test the function with examples
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
