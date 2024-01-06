#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    #  Get the first elements from tuples or 0 if tuples are too short
    a_0 = tuple_a[0] if len(tuple_a) >= 1 else 0
    b_0 = tuple_b[0] if len(tuple_b) >= 1 else 0

    #  Get the second elements from tuples or 0 if tuples are too short
    a_1 = tuple_a[1] if len(tuple_a) >= 2 else 0
    b_1 = tuple_b[1] if len(tuple_b) >= 2 else 0

    #  Return a tuple with the sum of the elements from both tuples
    return (a_0 + b_0, a_1 + b_1)
