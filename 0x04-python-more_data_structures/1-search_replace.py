#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.
    
    Args:
        my_list: The initial list
        search: The element to replace in the list
        replace: The new element
    
    Returns:
        A new list with all occurrences of 'search' replaced by 'replace'
    """
    return [replace if x == search else x for x in my_list]

# For testing the function
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    new_list = search_replace(my_list, 2, 89)
    print(new_list)
    print(my_list)
