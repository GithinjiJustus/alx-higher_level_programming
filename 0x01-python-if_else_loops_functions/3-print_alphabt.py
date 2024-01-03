#!/usr/bin/python3

# Print lowercase alphabet letters excluding positions 4 and 16#
for char in range(26):
    # Check if the character position is not 4 and not 16#
    if char != 4 and char != 16:
        # Convert the numerical value to its corresponding ASCII character#
        # Add the ASCII value of 'a' to the current value of 'char'#
        # Print the character without a newline (end="")#
        print("{:s}".format(chr(char + ord("a"))), end="")

