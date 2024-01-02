#!/usr/bin/python3

for char in range(26):
    # Check if the current character is not 'e' (char 4) & not 'q' (char 16)#
    if char != 4 and char != 16:
        # Print the character corresponding to the current number#
        print("{:s}".format(chr(char + ord("a"))), end="")
