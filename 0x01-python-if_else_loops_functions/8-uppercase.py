#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            letter = 32  # If character is lc, adjust its Unicode value to uc#
        else:
            letter = 0
        print("{:c}".format(ord(str[i]) - letter), end='')
        print()
