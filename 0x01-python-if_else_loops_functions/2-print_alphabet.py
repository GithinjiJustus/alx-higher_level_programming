#!/usr/bin/python3

for char in range(26):  # Iterate through each character in the range 0 to 25#
    print("{:s}".format(chr(char + ord("a"))), end="")  # Print the character#
