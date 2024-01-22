#!/usr/bin/python3
# This script defines a function safe_print_list_integers that prints integers from a list.

def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x integers of a list.

    Args:
        my_list (list): List containing any type of elements.
        x (int): Number of elements to access in my_list.

    Returns:
        int: The real number of integers printed.
    """
    nb_integers = 0  # Initialize the count of printed integers

    # Use try-except block to handle exceptions
    try:
        for i in range(x):
            if type(my_list[i]) == int:  # Check if the element is an integer
                print("{:d}".format(my_list[i]), end="")
                nb_integers += 1
    except IndexError:
        pass  # Ignore index errors
    
    print()  # Print a new line after the integers
    return nb_integers  # Return the real number of integers printed

# Test the function with examples
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
