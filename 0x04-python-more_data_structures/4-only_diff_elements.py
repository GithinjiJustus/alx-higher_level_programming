#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.
    
    Args:
        set_1: First set
        set_2: Second set
    
    Returns:
        A set containing elements that are present in only one of the sets
    """
    return set_1.symmetric_difference(set_2)

# For testing the function
if __name__ == "__main__":
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    od_set = only_diff_elements(set_1, set_2)
    print(sorted(list(od_set)))
