#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.
    
    Args:
        set_1: First set
        set_2: Second set
    
    Returns:
        A set containing common elements between set_1 and set_2
    """
    return set_1.intersection(set_2)

# For testing the function
if __name__ == "__main__":
    set_1 = { "Python", "C", "Javascript" }
    set_2 = { "Bash", "C", "Ruby", "Perl" }
    c_set = common_elements(set_1, set_2)
    print(sorted(list(c_set)))
