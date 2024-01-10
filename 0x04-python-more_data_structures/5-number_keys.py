#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    Returns the number of keys in a dictionary.
    
    Args:
        a_dictionary: Input dictionary
    
    Returns:
        The number of keys in the dictionary
    """
    return len(a_dictionary)

# For testing the function
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'number': 13, 'track': "Low level" }
    nb_keys = number_keys(a_dictionary)
    print("Number of keys: {:d}".format(nb_keys))
