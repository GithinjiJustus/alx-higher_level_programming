#!/usr/bin/python3

for i in range(100):
    # Check if the tens digit is not equal to the units digit
    if int(i / 10) != i % 10 and int(i / 10) < i % 10:
        # Print the pair of numbers (tens and units digits)
        print("{}{}".format(int(i / 10), i % 10), end="")
        # Check if it's not the number 89 to avoid adding a comma
        if (i != 89):
            print(", ", end="")

# Print a new line after all pairs are printed
print("")            
