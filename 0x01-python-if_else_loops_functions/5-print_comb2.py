#!/usr/bin/python3

# Loop through numbers from 0 to 99
for num in range(100):
    # Format the number with two digits (leading zero if needed)
    # If it's the last number, print with a newline
    print("{:02d}".format(num), end=", " if num != 99 else "\n")
