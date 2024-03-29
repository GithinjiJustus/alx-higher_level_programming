#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    
    Args:
        a_dictionary: Input dictionary
        key: Key to be replaced or added
        value: Value associated with the key
    
    Returns:
        The updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary

# For testing the function
if __name__ == "__main__":
    a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }
    new_dict = update_dictionary(a_dictionary, 'language', "Python")
    print(new_dict)
