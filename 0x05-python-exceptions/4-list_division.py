#!/usr/bin/python3
# This script defines a function list_division that divides two lists element-wise.

def list_division(my_list_1, my_list_2, list_length):
    """
    Divide element by element 2 lists.

    Args:
        my_list_1 (list): First list with elements of any type (integer, string, etc.).
        my_list_2 (list): Second list with elements of any type (integer, string, etc.).
        list_length (int): Desired length of the new list.

    Returns:
        list: A new list (length = list_length) with all divisions.
    """
    result_list = []  # Initialize the result list

    # Use try-except-finally block to handle exceptions
    for i in range(list_length):
        try:
            # Perform the division and append the result to the result_list
            result_list.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            # Handle division by 0
            print("division by 0")
            result_list.append(0)
        except (ValueError, TypeError):
            # Handle non-numeric elements
            print("wrong type")
            result_list.append(0)
        except IndexError:
            # Handle index out of range
            print("out of range")
            result_list.append(0)
        finally:
            pass  # Nothing specific to do in the finally section

    return result_list  # Return the new list with divisions

# Test the function with examples
if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
