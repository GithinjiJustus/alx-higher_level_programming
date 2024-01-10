#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).
    
    Args:
        my_list: The input list
    
    Returns:
        The sum of all unique integers in the list
    """
    return sum(set(my_list))

# For testing the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
