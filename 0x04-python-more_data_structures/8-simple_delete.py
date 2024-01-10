#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.
    
    Args:
        a_dictionary: Input dictionary
        key: Key to be deleted
    
    Returns:
        The updated dictionary after deleting the key-value pair (if exists)
    """
    a_dictionary.pop(key, None)
    return a_dictionary

# For testing the function
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
    new_dict = simple_delete(a_dictionary, 'track')
    print(new_dict)
