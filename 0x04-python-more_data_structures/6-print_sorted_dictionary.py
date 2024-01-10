#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.
    
    Args:
        a_dictionary: Input dictionary with string keys
    
    Prints:
        The dictionary's keys sorted in alphabetical order
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))

# For testing the function
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)
