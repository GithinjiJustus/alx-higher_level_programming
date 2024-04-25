#!/usr/bin/python3
""" 
This module contains a function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """ Finds a peak in a list of unsorted integers. """
    if not list_of_integers:
        return None
    
    peak = list_of_integers[0]
    for num in list_of_integers[1:]:
        if num > peak:
            peak = num
    return peak

if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
