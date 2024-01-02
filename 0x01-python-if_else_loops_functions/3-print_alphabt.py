#!/usr/bin/python3

for char in range(26):  #ASCII value#
    if char != 4 and char != 16:  #ASCII value denoted#
        print("{:s}".format(chr(char + ord("a"))), end="") #print ASCII#

